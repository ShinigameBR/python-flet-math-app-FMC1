import flet as ft

def linear_congruence(page):
    a = ft.TextField(label="a", width=((page.width / 3) - 40), height=50, text_size=20, text_align=ft.TextAlign.CENTER, border_color=ft.colors.DEEP_PURPLE_ACCENT_100, keyboard_type=ft.KeyboardType.NUMBER)
    b = ft.TextField(label="b", width=((page.width / 3) - 40), height=50, text_size=20, text_align=ft.TextAlign.CENTER, border_color=ft.colors.DEEP_PURPLE_ACCENT_100, keyboard_type=ft.KeyboardType.NUMBER)
    m = ft.TextField(label="m", width=((page.width / 3) - 40), height=50, text_size=20, text_align=ft.TextAlign.CENTER, border_color=ft.colors.DEEP_PURPLE_ACCENT_100, keyboard_type=ft.KeyboardType.NUMBER)
    result_output = ft.Text(size=18)

    def solve(e):
        try:
            x = int(a.value)
            y = int(b.value)
            n = int(m.value)
            solution = solve_congruence(x, y, n)
            if solution is None:
                result_output.value = "Não há solução."
            else:
                result_output.value = f"x ≡ {solution} (mod {n})"
        except ValueError:
            result_output.value = "Entradas inválidas. Por favor, insira números inteiros."
        page.update()

    return ft.View(route="/congruencia-linear", 
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                        title=ft.Text("Congruência Linear"),
                        bgcolor=ft.colors.SURFACE_VARIANT
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    a,
                                ]
                            ),
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("≡", size=50),
                                ]
                            ),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    b
                                ]
                            ),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    m,
                                ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(text="Resolver", on_click=solve),
                        ]
                    ),
                    ft.Row(
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            result_output,
                        ]
                    )
                ],
            )


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def multiplicative_inverse(a: int, m: int):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverso multiplicativo não existe se gcd(a, m) != 1
    else:
        return x % m

def solve_congruence(a: int, b: int, m: int):
    inv = multiplicative_inverse(a, m)
    if inv is None:
        return None  # Não há solução se o inverso multiplicativo não existe
    else:
        return (inv * b) % m