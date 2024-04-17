from flet import *
from adjustment.callyScore import main
import pages.FinalScoresPage
from pages.FinalScoresPage import FinalScoresPage


class create_course(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_hole = 1  
        self.scores = []  

        self.score_label = Text(
            "0",
            theme_style=TextThemeStyle.DISPLAY_MEDIUM,
            color='#FFFFFF',
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
        
        # Store values in session
        # page.session['total_score'] = total_score
        # page.session['callaway_score'] = callaway_score

        page.session.set('total_score', total_score)
        page.session.set('callaway_score', callaway_score)

        # Navigate to final_scores route
        page.go('/final_scores')







    def next_hole(self):
        current_score = int(self.score_label.value)
        if current_score != 0:
            self.scores.append(current_score)
        self.score_label.value = "0"
        self.current_hole += 1
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
        self.hole_label.update()

    def update(self):
        self.hole_label.value = f"Enter Score for Hole {self.current_hole}"
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
            current_score = int(self.score_label.value)
            if current_score == 0:
                print("Please enter a score greater than 0.")
                return  

            self.scores.append(current_score)
            self.score_label.value = "0"
            if self.current_hole < 18:
                self.next_hole()
            else:
                self.calculate_adjusted_score(self.page)

        return Column(
            controls=[
                Container(
                    height='100%',
                    width='100%',
                    padding=5,
                    margin=5,
                    bgcolor='#006400',  
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
                                alignment=alignment.center, 
                            ),
                            Container(
                                padding=5,
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
                                padding=10
                            ),
                        ]
                    )
                ),
            ]
        )

