from flet import *
import flet as ft

class full_eighteen(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1
        self.hole_pars = [0] * 18  # Initialize the list to store Par values for each hole

        # Define input_element as an instance attribute
        self.input_element = TextField(
            label=f"Par for Hole {self.current_hole}",
            on_change=lambda _: self.hole_input_changed()
        )

    def btn_click(self, e):
        if not self.input_element.value.isdigit():
            self.input_element.error_text = "Please enter a valid number"
            self.update()
        else:
            self.hole_pars[self.current_hole - 1] = int(self.input_element.value)
            self.next_hole_clicked()

    def next_hole_clicked(self):
        if self.current_hole < 18:
            self.current_hole += 1
            self.input_element.label = f"Par for Hole {self.current_hole}"
            self.input_element.value = str(self.hole_pars[self.current_hole - 1])
            self.update()

    def submit_pars(self):
        print("Par values for each hole:", self.hole_pars)
        return self.hole_pars  # Return the list of par values

    def build(self):
        return Column(
            controls=[
                Container(
                    height=1000,
                    width=1000,
                    padding=10,
                    margin=10,
                    bgcolor='#fdebd3',
                    content=Column(
                        controls=[
                            Container(
                                content=Text(
                                    f"Enter Par for Hole {self.current_hole}",
                                    theme_style=TextThemeStyle.DISPLAY_MEDIUM
                                ),
                                margin=10,
                                padding=10,
                            ),
                            Row(
                                [
                                    Text("Par:"),
                                    self.input_element  # Use the instance attribute
                                ],
                            ),
                            ElevatedButton(
                                "Submit",
                                on_click=lambda _: self.submit_pars()
                            ),
                            ElevatedButton(
                                "Next Hole",
                                on_click=lambda _: self.next_hole_clicked()
                            ),
                            ElevatedButton(
                                "Back",
                                on_click=lambda _: self.page.go('/type')
                            ),
                        ]
                    )
                )
            ]
        )

    def hole_input_changed(self):
        value = self.input_element.value
        if not value.isdigit():
            self.input_element.error_text = "Please enter a valid number"
        else:
            self.input_element.error_text = ""
            self.hole_pars[self.current_hole - 1] = int(value)

# ft.app(target=full_eighteen)
