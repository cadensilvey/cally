from flet import *

class create_course(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page



    def build(self):

        return Column(
            controls=[
                Container(
                    height=1000, 
                    width=1000,
                    padding=10,
                    margin=10,
                    bgcolor='#fdebd3',
                    content=Column(
                        controls=[
                            Container(
                                content=Text(
                                    "Create A Course",
                                    theme_style=TextThemeStyle.DISPLAY_MEDIUM
                                ), 
                                margin = 10,
                                padding = 10,                      
                                alignment= alignment.center,
                            ),
                            FilledTonalButton(     
                                # this page is taking the user to decide how they want to play.                            
                                on_click= lambda _: self.page.go('/18'),
                                text="18 Hole Course"
                            ),
                            FilledTonalButton(     
                                # this page is taking the user to decide how they want to play.                            
                                on_click= lambda _: self.page.go('/type'),
                                text="Play Golf"
                            ),
                            
                        ]
                    )
                )
            ]
        )