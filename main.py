import flet as ft
from components.views_handler import views_handler

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed="deeppurple")
    page.title = "Flowmath"

    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


    
ft.app(main)
