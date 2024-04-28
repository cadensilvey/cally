from flet import *
from adjustment.callyScore import main
from pages.FinalScoresPage import FinalScoresPage

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

    def calculate_adjusted_score(self, page):
        # Calculate total score
        total_score = sum(self.scores)
        
        # Calculate callaway score using callyScore.py
        callaway_score = main(self.scores)

        # Store the total_score and the cally_score in the session so they can be 
        # accessed in the finalScore page
        page.session.set('total_score', total_score)
        page.session.set('callaway_score', callaway_score)

        # Navigate to final_scores route
        page.go('/final_scores')

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
                self.update()
            else:
                self.calculate_adjusted_score(self.page)
            # Update the UI

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
                        ]
                    )
                ),
            ]
        )

