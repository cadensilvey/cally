from flet import *

class FinalScoresPage(UserControl):
    def __init__(self, total_score="Calculating...", callaway_score="Calculating..."):
        super().__init__()
        self.total_score = total_score
        self.callaway_score = callaway_score
        self.total_score_label = Text("Total Score:", theme_style=TextThemeStyle.DISPLAY_MEDIUM, color='#FFFFFF')
        self.callaway_score_label = Text("Callaway Score:", theme_style=TextThemeStyle.DISPLAY_MEDIUM, color='#FFFFFF')
        self.total_score_text = Text(str(self.total_score), theme_style=TextThemeStyle.DISPLAY_MEDIUM, color='#FFFFFF', text_align=alignment.center)
        self.callaway_score_text = Text(str(self.callaway_score), theme_style=TextThemeStyle.DISPLAY_MEDIUM, color='#FFFFFF', text_align=alignment.center)

    def build(self):
        return Container(
            height=1000,
            width=1000,
            padding=10,
            margin=10,
            bgcolor='#006400',  # Dark green color
            content=Column(
                controls=[
                    Container(
                        content=Icon(
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
                        content=self.total_score_label,
                        alignment=alignment.center
                    ),
                    Container(
                        padding=20,
                        margin=5,
                        content=self.total_score_text,
                        alignment=alignment.center
                    ),
                    Container(
                        padding=20,
                        margin=5,
                        content=self.callaway_score_label,
                        alignment=alignment.center
                    ),
                    Container(
                        padding=20,
                        margin=5,
                        content=self.callaway_score_text,
                        alignment=alignment.center
                    ),
                    # Container(
                    #     padding=20,
                    #     margin=5,
                    #     content=Column(
                    #         controls=[
                    #             self.total_score_label,
                    #             self.total_score_text,
                    #         ],
                    #         alignment=CrossAxisAlignment.CENTER,
                    #     ),
                    # ),
                    # Container(
                    #     padding=20,
                    #     margin=5,
                    #     content=Column(
                    #         controls=[
                    #             self.callaway_score_label,
                    #             self.callaway_score_text,
                    #         ],
                    #         alignment=CrossAxisAlignment.CENTER,
                    #     ),
                    # ),
                # alignment=CrossAxisAlignment.CENTER,
                    Container(
                        padding=20,
                        content=ElevatedButton(
                            on_click=lambda _: self.page.go('/'),
                            text="Go Home",
                            bgcolor='#FFFFFF',
                        ),
                        alignment=alignment.center,
                    ),
                ]

            )
        )
