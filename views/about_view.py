import flet as ft

def about_view(page):
    return ft.View(route="/sobre", 
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                        title=ft.Text("Sobre"),
                        bgcolor=ft.colors.SURFACE_VARIANT
                    ),
                    ft.Text("Feito com amor por Expedito Hebert.")
                ],
            )
