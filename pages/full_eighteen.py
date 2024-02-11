from flet import *

class full_eighteen(UserControl):
    par_text_field = TextField(label="Enter Par for Hole 1")

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1
        self.hole_pars = [0] * 18
        self.total_par_text = Text()  # Initialize without setting the initial text
        self.update_total_par_text()  # Set the initial text for the total par

    def build(self):
        text_container = Container(
            content=Text(
                "Enter Course Details: ",
                theme_style=TextThemeStyle.DISPLAY_SMALL,
                color=colors.BLACK,
            ),
            margin=10,
            padding=30,
            alignment=alignment.center,
        )


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
                            text_container,
                            Container(
                                content=self.par_text_field,
                                padding=10,
                                alignment=alignment.center,
                            ),
                            ElevatedButton(
                                "Next Hole",
                                on_click=lambda _: self.next_hole(),
                                # alignment=alignment.center
                            ),
                            Container(
                                self.total_par_text,
                                alignment=alignment.center,
                            ),
                        ]
                    )
                )
            ]
        )

    def update_par(self, value):
        try:
            value = int(value)
            print("Par value is a digit")
            self.hole_pars[self.current_hole - 1] = value
            print(f"Par for Hole {self.current_hole}: {self.hole_pars[self.current_hole - 1]}")
            self.update_total_par_text()  # Update total par when a new value is entered
        except ValueError:
            print("Please enter a valid number.")

    def next_hole(self):
        if 1 <= self.current_hole <= 18:
            entered_value = self.par_text_field.value
            self.update_par(entered_value)
            self.current_hole += 1
            self.update_text_field_label()
            self.update()  # Trigger a UI update
        else:
            print("Submitted Pars:", self.hole_pars)

    def update_text_field_label(self):
        print("Updating text field")
        self.par_text_field.label = f"Enter Par for Hole {self.current_hole}"

    def update_total_par_text(self):
        # Update the total par Text control
        self.total_par_text.value = f"Total Par: {sum(self.hole_pars)}"
