from flet import *
from pages.home import home
from pages.type_play import type_play
from pages.choose_course import choose_course
from pages.create_course import create_course
from pages.full_eighteen import full_eighteen

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
        '/create' :View(
            route='/create',
            controls=[
                create_course(page)
            ]
        ),
        '/18' :View(
            route='/18',
            controls=[
                full_eighteen(page)
            ]
        ),
    }