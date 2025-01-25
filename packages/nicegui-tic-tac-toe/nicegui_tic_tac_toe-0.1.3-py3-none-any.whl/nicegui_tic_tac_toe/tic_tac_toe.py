from typing import Literal

from nicegui import ui

type State = Literal["X", "O", ""]  # マスの状態または手番


class Square(ui.element):
    """GUI部品としてのマス"""

    def __init__(self, click, index: int):
        super().__init__("div")
        self.click = click  # ボタンのクリック用
        self.button_text = str(index)  # ボタンの番号
        self.value: State = ""  # マスの値

    def build(self, value: State) -> None:
        """GUI作成"""
        self.clear()  # 子要素をクリア
        self.value = value
        with self:
            # 値があるときはアイコンを、ないときはボタンを表示
            if self.value:
                name = "close" if self.value == "X" else "radio_button_unchecked"
                color = "red" if self.value == "X" else "indigo-4"
                self.icon = ui.icon(name, size="3em", color=color).classes("size-10")
            else:
                ui.button(self.button_text, on_click=self.click).classes("rounded-xl size-10 bg-cyan-2")


class Game:
    """三目並べゲーム"""

    player: State  # 手番
    squares: list[Square]  # 9つのマス
    message: str = ""  # 手番や勝敗の表示

    def __init__(self):
        with ui.column().style("margin: 0 auto"):
            self.squares = []  # 9つのSquareのリスト
            # self.messageにバインドするメッセージ
            ui.label().bind_text(self, "message").classes("text-4xl")
            with ui.card().classes("bg-cyan-1"):
                for i in range(3):
                    with ui.row():
                        self.squares.extend([Square(self.click, i * 3 + j) for j in range(3)])
            ui.button("reset", icon="refresh", on_click=self.reset).props("flat")
            self.reset()

    def reset(self) -> None:
        """ゲームの初期化"""
        self.player: State = "O"
        self.message = f"{self.player}'s turn"
        for square in self.squares:
            square.build("")  # Squareの再作成

    def click(self, event) -> None:
        """マスのクリック"""
        if "won" not in self.message:
            self.squares[int(event.sender.text)].build(self.player)
            self.player = "X" if self.player == "O" else "O"
            self.judge()

    def judge(self) -> None:
        """終局判定"""
        for target in [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]:
            values = "".join(self.squares[i].value or "." for i in target)
            if values in {"OOO", "XXX"}:
                self.message = f"{values[0]} has won!"
                for i in range(9):
                    if i not in target and hasattr(self.squares[i], "icon"):
                        self.squares[i].icon.classes("opacity-20")  # 揃ってないアイコンを薄くする
                break
        else:
            if all(square.value for square in self.squares):
                self.message = "draw"
            else:
                self.message = f"{self.player}'s turn"


def main(*, reload=False, port=8101):
    Game()
    ui.run(title="TicTacToe", reload=reload, port=port)
