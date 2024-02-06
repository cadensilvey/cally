from flet import *
from pages.home import home
from pages.type_play import type_play
from pages.choose_course import choose_course

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
        '/choose' :View(
            route='/choose',
            controls=[
                choose_course(page)
            ]
        ),
    }