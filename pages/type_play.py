from flet import *


class type_play(UserControl):
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
                                    "How Do You Want To Play",
                                    theme_style=TextThemeStyle.DISPLAY_SMALL
                                ), 
                                margin = 10,
                                padding = 10,                      
                                alignment= alignment.center,
                            ),
                            FilledTonalButton(     
                                # this is taking the user to create a course                           
                                on_click= lambda _: self.page.go('/create'),
                                text="Create Course",
                            ),
                            FilledTonalButton(     
                                # this is taking the user to choose the course they want to play                           
                                on_click= lambda _: self.page.go('/choose'),
                                text="Choose Course",
                            ),
                            FilledTonalButton(     
                                # take the user back home                            
                                on_click= lambda _: self.page.go('/'),
                                text="Go Back Home ",
                            ),
                            
                        ]
                    )
                )
            ]
        )  
    
        