from flet import *

class home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    height=1000,
                    width=1000,
                    padding=5,
                    margin=5,
                    bgcolor='#006400',  # Dark green color
                    content=Column(
                        controls=[
                            Container(
                                content=
                                    Icon(
                                        name=icons.GOLF_COURSE,
                                        color='#fdebd3',
                                        size=50,
                                    ),
                                padding=50,
                                alignment=alignment.center,  # Center the icon horizontally and vertically
                            ),
                            Container(
                                content=Text(
                                    "Cally",
                                    theme_style=TextThemeStyle.DISPLAY_LARGE,
                                    color='#fdebd3',
                                ),
                                margin=10,
                                padding=40,
                                alignment=alignment.center,
                            ),
                            Container(
                                content=ElevatedButton(
                                    on_click=lambda _: self.page.go('/create'),
                                    text="Play Golf",
                                    bgcolor='#fdebd3',  # Teal color
                                ),
                                alignment=alignment.center,  # Center the button horizontally
                            ),
                        ]
                    )
                )
            ]
        )
