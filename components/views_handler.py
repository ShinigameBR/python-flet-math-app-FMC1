import flet as ft
from views.home_view import home_view
from views.about_view import about_view
from views.linear_congruence import linear_congruence
from views.congruence_system import congruence_system

def views_handler(page):
    return{
        "/": home_view(page),
        "/sobre": about_view(page),
        "/congruencia-linear": linear_congruence(page),
        "/sistema-de-congruencias": congruence_system(page),
    }


