import tomllib
from collections.abc import Iterator
from enum import IntEnum
from pathlib import Path
from typing import ClassVar

import numpy as np
from nicegui import elements, ui


class State(IntEnum):
    Empty = 0
    Black = 1
    White = 2
    OK = 3  # 手番で置けるか

    def opponent(self) -> "State":
        """Black <-> White"""
        return State.Black if self == State.White else State.White


def ok_to_empty[T](board: T) -> T:  # Tはintまたはnp.ndarray
    """State.OK(3)であればState.Empty(0)に変換する"""
    return board % 3  # type: ignore[operator, return-value]


class Square(ui.element):
    chars: ClassVar[list[str]] = ["", "⚫️", "⚪️", "・"]

    def __init__(self, reversi: "Reversi", index: int):
        super().__init__("div")
        self.reversi = reversi
        self.index = index  # 左上が1+1*9、右下が8+8*9

    def build(self, value: State) -> None:
        """UI作成"""
        self.clear()  # 子要素をクリア
        with self:
            classes = "w-9 h-9 text-3xl text-center border border-black"
            ui.label(self.chars[value]).classes(classes).on("click", lambda: self.reversi.click(self))


class Reversi:
    player: State = State.Black  # 手番
    board: np.ndarray  # 10*9+1個のint8の1次元配列
    message: str = ""  # 手番や勝敗の表示
    squares: list[Square]  # 64個のマス
    pass_button: elements.button.Button  # PASSボタン
    SAVE_FILE: ClassVar[str] = "reversi.toml"  # ファイル名

    def __init__(self):
        with ui.card(align_items="center"):
            ui.label().bind_text(self, "message").classes("text-3xl")
            with ui.grid(columns=8).classes("gap-0 bg-green"):
                self.squares = [Square(self, x + y * 9) for y in range(1, 9) for x in range(1, 9)]
            with ui.row():
                ui.button("Reset", on_click=self.reset)
                self.pass_button = ui.button("Pass", on_click=self.pass_)
                self.pass_button.disable()
                ui.button("Load", on_click=self.load)
                ui.button("Save", on_click=self.save)
        self.reset()

    def reset(self) -> None:
        """ゲームの初期化"""
        self.set_player(State.Black)
        self.board = np.full(91, State.Empty, dtype=np.int8)
        self.board[41:51:8] = State.Black
        self.board[40:52:10] = State.White
        self.rebuild()

    def set_player(self, player: State) -> None:
        """手番設定"""
        self.player = player
        self.message = f"{self.player.name}'s turn"

    @classmethod
    def set_ok(cls, player: State, board: np.ndarray) -> bool:
        """置けるマスをチェックし、置けるかを返す"""
        for y in range(1, 9):
            for x in range(1, 9):
                index = x + y * 9
                if not ok_to_empty(board[index]):  # Empty or OK
                    exist_ok = any(cls.calc_last_and_diff(index, player, board))
                    board[index] = State.OK if exist_ok else State.Empty
        return (board == State.OK).any()  # 置けるマスがあるかどうか

    def rebuild(self) -> None:
        """置けるマスをチェックし、Squareの再作成"""
        exist_ok = self.set_ok(self.player, self.board)
        for square in self.squares:
            square.build(self.board[square.index])
        self.pass_button.set_enabled(not exist_ok)

    def pass_(self) -> None:
        """パス処理"""
        self.set_player(self.player.opponent())
        self.set_ok(self.player, self.board)
        self.rebuild()

    def to_toml(self) -> str:
        """ゲームの状態をTOML化"""
        lst = [f'player = "{self.player.name}"', "board = ["]
        for i in range(1, 9):
            s, e = i * 9 + 1, i * 9 + 9
            lst.append(f"  {ok_to_empty(self.board[s:e]).tolist()},")
        lst.append("]")
        return "\n".join(lst)

    def from_toml(self, toml: str) -> None:
        """TOMLからゲームの状態を復元"""
        dc = tomllib.loads(toml)
        self.set_player(State[dc["player"]])
        board = np.full((10, 9), State.Empty, dtype=np.int8)
        board[1:9, 1:9] = dc["board"]
        self.board = np.hstack([board.flatten(), [0]])
        self.rebuild()
        self.judge()

    def save(self) -> None:
        """ゲームの状態をファイルに保存"""
        Path(self.SAVE_FILE).write_text(self.to_toml(), encoding="utf-8")

    def load(self) -> None:
        """ファイルからゲームの状態を読込"""
        self.from_toml(Path(self.SAVE_FILE).read_text(encoding="utf-8"))

    def click(self, target: Square) -> None:
        """マスのクリック"""
        if ok_to_empty(self.board[target.index]) != State.Empty or not self.place_disk(target.index):
            return
        self.board[target.index] = self.player
        self.set_player(self.player.opponent())
        self.rebuild()
        self.judge()

    def judge(self) -> None:
        """終局判定"""
        if (ok_to_empty(self.board) == State.Empty).any():  # 空きマスあり
            if not self.pass_button.enabled:  # 置けるマスあり
                return
            board = self.board.copy()
            if self.set_ok(self.player.opponent(), board):  # 相手は置ける
                return
        self.pass_button.disable()
        n_black = (self.board == State.Black).sum()
        n_white = (self.board == State.White).sum()

        self.message = (
            "Draw"
            if n_black == n_white
            else f"Black won!({n_black} > {n_white})"
            if n_black > n_white
            else f"White won!({n_white} > {n_black})"
        )

    @classmethod
    def calc_last_and_diff(cls, index: int, player: State, board: np.ndarray) -> Iterator[tuple[int, int]]:
        """indexに置いたとき、8方向ごとにどれだけひっくり返せるか

        diffが方向
        lastが挟むための自分のディスクの位置
        """
        opponent = player.opponent()
        for diff in [-10, -9, -8, -1, 1, 8, 9, 10]:
            for cnt in range(1, 9):
                last = index + diff * cnt
                value = board[last]
                if value != opponent:
                    if cnt > 1 and value == player:
                        yield last, diff
                    break

    def place_disk(self, index: int) -> bool:
        """ディスクを置く"""
        last_and_diffs = list(self.calc_last_and_diff(index, self.player, self.board))
        if not last_and_diffs:
            return False
        self.board[index] = self.player
        for last, diff in last_and_diffs:
            self.board[index:last:diff] = self.player
        return True


def main(*, reload=False, port=8102):
    Reversi()
    ui.run(title="Reversi", reload=reload, port=port)
