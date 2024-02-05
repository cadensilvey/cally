from flet import *

class home(UserControl):
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
                                    "Cally",
                                    theme_style=TextThemeStyle.DISPLAY_MEDIUM
                                ), 
                                margin = 10,
                                padding = 10,                      
                                alignment= alignment.center,
                            ),
                            
                            FilledTonalButton(
                                
                                on_click= lambda _: self.page.go('/type'),
                                text="Play Golf"
                                # need to make new page here to play golf 
                            ),
                            
                        ]
                    )
                )
            ]
        )