from flet import *

class FinalScoresPage(UserControl):
    def __init__(self, total_score="Calculating...", callaway_score="Calculating..."):
        super().__init__()
        self.total_score = total_score
        self.callaway_score = callaway_score
        self.total_score_text = Text(f"Total Score: {self.total_score}", theme_style=TextThemeStyle.DISPLAY_LARGE, color='#FFFFFF', text_align=alignment.center)
        self.callaway_score_text = Text(f"Callaway Adjusted Score: {self.callaway_score}", theme_style=TextThemeStyle.DISPLAY_LARGE, color='#FFFFFF', text_align=alignment.center)

    def build(self):
        return Container(
            content=Column(
                controls=[
                    self.total_score_text,
                    self.callaway_score_text,
                    Container(
                        content=ElevatedButton(
                            on_click=lambda _: self.page.go('/'),
                            text="Go Back",
                            bgcolor='#FFFFFF',
                        ),
                        alignment=alignment.center,
                    ),
                ]
            ),
            bgcolor='#006400',  # Set background color to match create_course page
        )







