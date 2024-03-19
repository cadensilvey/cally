from flet import *
from adjustment.callyScore import main, intSplit, handicapAdjustment, initDeduction

class create_course(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1  # Initialize the current hole to 1
        self.pars = []  # Initialize an empty list to store pars
        self.scores = []  # Initialize an empty list to store scores
        # Define text fields for par and score input
        self.tb_par = TextField(label="Par", value="")
        self.tb_score = TextField(label="Score", value="")
        self.hole_label = Text(
            f"Enter Par and Score for Hole {self.current_hole}",
            theme_style=TextThemeStyle.DISPLAY_MEDIUM,
            text_align=alignment.top_center
        )
        self.total_score_label = Text(
            "",
            theme_style=TextThemeStyle.DISPLAY_MEDIUM,
            text_align=alignment.top_center
        )
        self.callaway_score_label = Text(
             "",
             theme_style=TextThemeStyle.DISPLAY_SMALL,
             text_align=alignment.bottom_center
        )




    def calculate_adjusted_score(self):
        total_score = sum(self.scores)
        self.total_score_label.value = f"Total Score: {total_score}"
        
        # Calculate Callaway adjusted score using the main function from callyScore.py
        callaway_score = main(self.scores)
        
        # Update the callaway_score_label with the calculated Callaway adjusted score
        self.callaway_score_label.value = f"Callaway Adjusted Score: {callaway_score}"


    def next_hole(self):
        # Increment the current hole number and clear the text fields
        self.current_hole += 1
        self.hole_label.value = f"Enter Par and Score for Hole {self.current_hole}"
        self.tb_par.value = ""
        self.tb_score.value = ""
        self.hole_label.update()

    def update(self):
        # Update the hole label text to reflect the current hole number
        self.hole_label.value = f"Enter Par and Score for Hole {self.current_hole}"
        # Update the text fields to reflect any changes in their values
        self.tb_par.update()
        self.tb_score.update()
        self.total_score_label.update()
        self.callaway_score_label.update()


    def build(self):
        def button_clicked(e):
            # Check if the text fields are not empty before appending to the lists
            if self.tb_par.value.strip() and self.tb_score.value.strip():
                self.pars.append(int(self.tb_par.value))
                self.scores.append(int(self.tb_score.value))
                # Clear the text fields for the next hole
                if self.current_hole < 18:
                    self.next_hole()
                else:
                    self.calculate_adjusted_score()
                # Call the update method to refresh the UI
                self.update()
            else:
                print("Please enter both par and score before proceeding.")

        return Column(
            controls=[
                Container(
                    height=1000,
                    width=1000,
                    padding=5,
                    margin=5,
                    content=Column(
                        controls=[
                            Container(
                                content=self.hole_label,
                            ),
                            self.tb_par,
                            self.tb_score,
                            Container(
                                content=ElevatedButton(
                                    text="Next Hole" if self.current_hole < 18 else "Calculate Adjusted Score",
                                    on_click=button_clicked,
                                    bgcolor='#fdebd3',  # Teal color
                                ),
                                padding=5
                            ),
                            self.total_score_label,  # Add total score label here
                            self.callaway_score_label, # Callaway Adjusted Score 
                        ]
                    )
                ),
            ]
        )
