from flet import *

class type_play(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    height=800, 
                    width=300,
                    bgcolor='green',
                    content=Column(
                        controls=[
                            Text('What type of course would you like to play?'),
                            Container(
                                on_click= lambda _: self.page.go('/') ,
                                content=Text('Go back a page', size=25,
                                            color='black')
                            )
                        ]
                    )
                )
            ]
        )