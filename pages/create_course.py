from flet import *
from adjustment.callyScore import main

class create_course(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1  # Initialize the current hole to 1
        self.scores = []  # Initialize an empty list to store scores
        # Define text field for score input
        self.tb_score = TextField(label="Score", value="")
        self.hole_label = Text(
            f"Enter Score for Hole {self.current_hole}",
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
        # Increment the current hole number and clear the text field
        self.current_hole += 1
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
        self.tb_score.value = ""
        self.hole_label.update()

    def update(self):
        # Update the hole label text to reflect the current hole number
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
        # Update the text field for score to reflect any changes in its value
        self.tb_score.update()
        self.total_score_label.update()
        self.callaway_score_label.update()

    def build(self):
        def button_clicked(e):
            # Check if the text field is not empty before appending to the list
            if self.tb_score.value.strip():
                self.scores.append(int(self.tb_score.value))
                # Clear the text field for the next hole
                if self.current_hole < 18:
                    self.next_hole()
                else:
                    self.calculate_adjusted_score()
                # Call the update method to refresh the UI
                self.update()
            else:
                print("Please enter the score before proceeding.")

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
                            self.tb_score,
                            Container(
                                content=ElevatedButton(
                                    text="Next Hole" if self.current_hole < 18 else "Calculate Adjusted Score",
                                    on_click=button_clicked,
                                    bgcolor='#fdebd3',  # Teal color
                                ),
                                alignment=alignment.center, # center this button horizontally 
                                padding=5
                            ),
                            Container(
                                content=ElevatedButton(
                                    on_click=lambda _: self.page.go('/'),
                                    text="Go Home",
                                    bgcolor='#fdebd3',  # Teal color
                                ),
                                alignment=alignment.center,  # Center the button horizontally
                            ),
                            self.total_score_label,  # Add total score label here
                            self.callaway_score_label, # Callaway Adjusted Score 
                        ]
                    )
                ),
            ]
        )
