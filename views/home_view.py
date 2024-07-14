import flet as ft

def home_view(page):
    return ft.View(route="/",
                controls=[
                    ft.AppBar(
                        title=ft.Text("Flowmath"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        actions=[
                            ft.IconButton(ft.icons.DARK_MODE_ROUNDED, on_click=lambda e: switch(page, e)),
                            ft.IconButton(ft.icons.INFO_ROUNDED, on_click=lambda _: page.go("/sobre")),
                        ]
                    ),
                    ft.Row(
                        wrap=True,
                        controls=[
                            ft.ElevatedButton("Congruência Linear", on_click=lambda _: page.go("/congruencia-linear")),
                            ft.ElevatedButton("Sistema de Congruência", on_click=lambda _: page.go("/sistema-de-congruencias")),
                        ]
                    ),
                ],
            )

def switch(page: ft.Page, toggle: ft.IconButton) -> None:
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            toggle.icon = ft.icons.LIGHT_MODE_ROUNDED

        else:
            page.theme_mode = ft.ThemeMode.DARK
            toggle.icon = ft.icons.DARK_MODE_ROUNDED

        page.update()
