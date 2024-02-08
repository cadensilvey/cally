from flet import *

class type_play(UserControl):
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
                "How Do You Want To Play",
                theme_style=TextThemeStyle.DISPLAY_MEDIUM,
                color='#fdebd3',
            ),
            margin=10,
            padding=30,
            alignment=alignment.center,
        )

        create_button = Container(
            content=ElevatedButton(
                on_click=lambda _: self.page.go('/create'),
                text="Create Course",
                bgcolor='#fdebd3',  # Teal color
            ),
            padding=5,
            alignment=alignment.center,  # Center the button horizontally
        )

        search_button = Container(
            content=ElevatedButton(
                on_click=lambda _: self.page.go('/choose'),
                text="Search Course",
                bgcolor='#fdebd3',  # Teal color
            ),
            padding=5,
            alignment=alignment.center,  # Center the button horizontally
        )

        home_button = Container(
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
                            create_button,
                            search_button,
                            home_button,
                        ]
                    )
                )
            ]
        )
