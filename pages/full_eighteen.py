from flet import *
# from flet.controls import UserControl

class full_eighteen(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.counter = 0
        self.text = Text(str(self.counter))

    def add_click(self, page):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def subtract_click(self, page):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        return Row(
            [ElevatedButton("-", on_click=self.subtract_click),self.text, ElevatedButton("+", on_click=self.add_click)]
        )
