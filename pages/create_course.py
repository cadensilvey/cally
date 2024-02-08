from flet import *

class create_course(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        icon_container = Container(
            content=Icon(
                name=icons.GOLF_COURSE,
                color='#fdebd3',
                size=50,
            ),
            padding=10,
            alignment=alignment.center,  # Center the icon horizontally and vertically
        )

        text_container = Container(
            content=Text(
                "Create A Course",
                theme_style=TextThemeStyle.DISPLAY_MEDIUM,
                color='#fdebd3',
            ),
            margin=10,
            padding=30,
            alignment=alignment.center,
        )

        full_course = Container(
            content=ElevatedButton(
                on_click=lambda _: self.page.go('/18'),
                text="18 Holes",
                bgcolor='#fdebd3',  # Teal color
            ),
            padding=5,
            alignment=alignment.center,  # Center the button horizontally
        )

        front_nine = Container(
            content=ElevatedButton(
                on_click=lambda _: self.page.go('/'),
                text="9 Holes - (no work)",
                bgcolor='#fdebd3',  # Teal color
            ),
            padding=5,
            alignment=alignment.center,  # Center the button horizontally
        )

        back_button = Container(
            content=ElevatedButton(
                on_click=lambda _: self.page.go('/'),
                text="Go Back Home",
                bgcolor='#fdebd3',  # Teal color
            ),
            padding=5,
            alignment=alignment.center,  # Center the button horizontally
        )

        return Column(
            controls=[
                Container(
                    height=1000,
                    width=1000,
                    padding=10,
                    margin=10,
                    bgcolor='#006400',
                    content=Column(
                        controls=[
                            icon_container,
                            text_container,
                            full_course,
                            front_nine,
                            back_button,
                        ]
                    )
                )
            ]
        )
