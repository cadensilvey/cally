from flet import *

class full_eighteen(UserControl):
    par_text_field = TextField(label="Enter Par for Hole 1")

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1
        self.hole_pars = [0] * 18

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
                                content=self.par_text_field,
                                padding=10,
                                alignment=alignment.center,
                            ),
                            ElevatedButton(
                                "Next Hole",
                                on_click=lambda _: self.next_hole()
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
        except ValueError:
            print("Please enter a valid number.")

    def next_hole(self):
        if 1 <= self.current_hole <= 18:
            entered_value = self.par_text_field.value  # Get the entered value directly
            self.update_par(entered_value)
            self.current_hole += 1
            self.update_text_field_label()
            self.update()  # Trigger a UI update
        else:
            print("Submitted Pars:", self.hole_pars)

    def update_text_field_label(self):
        print("Updating text field")
        self.par_text_field.label = f"Enter Par for Hole {self.current_hole}"

# Create an instance of the page
# page_instance = full_eighteen(None)

# # Simulate the entry of values into the text field
# for entered_value in ["3", "4", "5", "2", "3", "4", "2", "5", "3", "4", "3", "2", "4", "5", "3", "4", "2", "3"]:
#     page_instance.par_text_field.set_value(entered_value)
#     page_instance.next_hole()
