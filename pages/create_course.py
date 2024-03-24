from flet import *
from adjustment.callyScore import main

class create_course(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1  # Initialize the current hole to 1
        self.scores = []  # Initialize an empty list to store scores
        # Define label for score display
        self.score_label = Text(
            "0",
            theme_style=TextThemeStyle.DISPLAY_MEDIUM,
            color='#FFFFFF',
            # id='score_label'
        )
        self.hole_label = Text(
            f"Enter Score for Hole {self.current_hole}",
            theme_style=TextThemeStyle.DISPLAY_MEDIUM,
            color='#FFFFFF',
        )
        self.total_score_label = Text(
            "",
            color='#FFFFFF',
            theme_style=TextThemeStyle.DISPLAY_SMALL,
            text_align=alignment.center,
        )
        self.callaway_score_label = Text(
            "",
            color='#FFFFFF',
            theme_style=TextThemeStyle.DISPLAY_SMALL,
            text_align=alignment.center,
        )

    def calculate_adjusted_score(self):
        total_score = sum(self.scores)
        self.total_score_label.value = f"Total Score: {total_score}"
        
        # Calculate Callaway adjusted score using the main function from callyScore.py
        callaway_score = main(self.scores)
        
        # Update the callaway_score_label with the calculated Callaway adjusted score
        self.callaway_score_label.value = f"Callaway Adjusted Score: {callaway_score}"

    def next_hole(self):
        # Save the score for the current hole only if it's not zero
        current_score = int(self.score_label.value)
        if current_score != 0:
            self.scores.append(current_score)
        # Print the list of scores
        print("List of Scores:", self.scores)
        # Clear the score label for the next hole
        self.score_label.value = "0"
        
        # Increment the current hole number and update the hole label
        self.current_hole += 1
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
        self.hole_label.update()

    def update(self):
        # Update the hole label text to reflect the current hole number
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
        # Update the score label to reflect any changes in its value
        self.score_label.update()
        self.total_score_label.update()
        self.callaway_score_label.update()

    def build(self):
        def increase_score(_):
            current_score = int(self.score_label.value)
            self.score_label.value = str(current_score + 1)
            self.update()

        def decrease_score(_):
            current_score = int(self.score_label.value)
            if current_score > 0:
                self.score_label.value = str(current_score - 1)
                self.update()

        def button_clicked(e):
            # Check if the entered score is zero
            current_score = int(self.score_label.value)
            if current_score == 0:
                print("Please enter a score greater than 0.")
                return  # Exit the method without proceeding to the next hole

            # Save the score for the current hole
            self.scores.append(current_score)
            # Clear the score label for the next hole
            self.score_label.value = "0"
            # Proceed to the next hole or calculate the adjusted score
            if self.current_hole < 18:
                self.next_hole()
            else:
                self.calculate_adjusted_score()
            # Update the UI
            self.update()

        return Column(
            controls=[
                Container(
                    height=1000,
                    width=1000,
                    padding=10,
                    margin=10,
                    bgcolor='#006400',  # Dark green color
                    content=Column(
                        controls=[
                            Container(
                                content=
                                    Icon(
                                        name=icons.GOLF_COURSE,
                                        color='#FFFFFF',
                                        size=50,
                                    ),
                                padding=5,
                                alignment=alignment.center,  # Center the icon horizontally and vertically
                            ),
                            Container(
                                padding=20,
                                margin=5,
                                content=self.hole_label,
                                alignment=alignment.center,
                            ),
                            Row(
                                controls=[
                                    Container(
                                        content=ElevatedButton(
                                            text="-",
                                            on_click=decrease_score,
                                            bgcolor='#FFFFFF',
                                        ),
                                        alignment=alignment.center_left
                                    ),
                                    Container(
                                        content=self.score_label,
                                        alignment=alignment.center
                                    ),
                                    Container(
                                        content=ElevatedButton(
                                            text="+",
                                            on_click=increase_score,
                                            bgcolor='#FFFFFF',
                                        ),
                                        alignment=alignment.center_right
                                    ),
                                ],
                                alignment=MainAxisAlignment.SPACE_AROUND
                            ),
                            Container(
                                content=ElevatedButton(
                                    text="Next Hole" if self.current_hole < 18 else "Calculate Adjusted Score",
                                    on_click=button_clicked,
                                    bgcolor='#FFFFFF',
                                ),
                                alignment=alignment.center,
                                padding=20
                            ),
                            Container(
                                content=ElevatedButton(
                                    on_click=lambda _: self.page.go('/'),
                                    text="Go Home",
                                    bgcolor='#FFFFFF',
                                ),
                                alignment=alignment.center,
                            ),
                            self.total_score_label,
                            self.callaway_score_label,
                        ]
                    )
                ),
            ]
        )
