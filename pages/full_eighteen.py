from flet import *

class full_eighteen(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1
        self.hole_pars = [0] * 18
        self.hole_scores = [0] * 18

    def btn_click(self, e):
        par_text_field = self.get_par_text_field()
        score_text_field = self.get_score_text_field()

        # if (
        #     not par_text_field.value
        #     or not par_text_field.value.isdigit()
        #     or not score_text_field.value
        #     or not score_text_field.value.isdigit()
        # ):
        #     par_text_field.error_text = "Please enter valid numbers"
        #     score_text_field.error_text = "Please enter valid numbers"
        # else:
        self.hole_pars[self.current_hole - 1] = int(par_text_field.value)
        self.hole_scores[self.current_hole - 1] = int(score_text_field.value)
        self.next_hole_clicked()

    def next_hole_clicked(self, _=None):
        print("doing an update")
        print("Controls:\n\n", self.controls)
        self.update()

        if self.current_hole < 18:
            self.update()
            print("Next Hole Clicked")  # Add this line for debugging
            self.current_hole += 1
            self.update_text_fields()

    def update_text_fields(self):
        par_text_field = self.get_par_text_field()
        score_text_field = self.get_score_text_field()

        if par_text_field is None or score_text_field is None:
            print("Error: Text fields not found.")
            return

        print("this is what the text fields say : \n")
        print(f"par_text_field: {par_text_field}")
        print(f"score_text_field: {score_text_field}")

        par_text_field= f"Par for Hole {self.current_hole}"
        score_text_field = f"Score for Hole {self.current_hole}"

        # Save the entered values to the lists
        self.hole_pars[self.current_hole - 1] = int(par_text_field)
        self.hole_scores[self.current_hole - 1] = int(score_text_field)

        # Check if all holes are filled
        if self.current_hole == 18:
            print("Pars:", self.hole_pars)
            print("Scores:", self.hole_scores)
        else:
            # Update for the next hole
            self.current_hole += 1
            self.update()  # Update the UI based on your framework





    def get_par_text_field(self):
        return self.controls[1] if len(self.controls) > 1 else None

    def get_score_text_field(self):
        return self.controls[2] if len(self.controls) > 2 else None



    def build(self):
        par_text_field = TextField(label=f"Par for Hole {self.current_hole}")
        score_text_field = TextField(label=f"Score for Hole {self.current_hole}")

        self.controls = [
            Container(content=Text(
                f"Enter Par and Score for Hole {self.current_hole}",
                theme_style=TextThemeStyle.DISPLAY_MEDIUM
            )),
            Container(content=Row(controls=[Text("Par:"), par_text_field])),
            Container(content=Row(controls=[Text("Score:"), score_text_field])),
            ElevatedButton(
                "Submit",
                on_click=self.btn_click
            ),
            ElevatedButton(
                "Next Hole",
                on_click=self.next_hole_clicked
            ),
        ]

        print("Controls:\n\n", self.controls)
        return Column(controls=self.controls)



