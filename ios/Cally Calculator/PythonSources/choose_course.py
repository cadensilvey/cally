from flet import *

class choose_course(UserControl):
    def __init__(self,page):
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
                    bgcolor='#679186',
                    content=Column(
                        controls=[
                            Container(
                                content=Text(
                                    "Choose Course",
                                    theme_style=TextThemeStyle.DISPLAY_MEDIUM,
                                    text_align=alignment.top_center
                                ),
                            ),
                            SearchBar(
                                view_elevation=4,
                                divider_color=colors.AMBER,
                                bar_hint_text="Search course",
                                view_hint_text="type here to search...",
                            )
                        ]
                    )
                ),
            ]
        )