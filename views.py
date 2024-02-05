from flet import *
from pages.home import home
from pages.type_play import type_play

def views_handler(page):
    return {
        '/' :View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        '/type' :View(
            route='/type',
            controls=[
                type_play(page)
            ]
        ),
    }