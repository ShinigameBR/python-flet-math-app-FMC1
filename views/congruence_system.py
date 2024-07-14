import flet as ft
from functools import reduce

def congruence_system(page):
    relations_inputs = []
    result_output = ft.Text(size=18)

    def add_case():
        relation = ft.Row(
            controls=[
                ft.TextField(label="a", width=((page.width / 3) - 40), height=50, text_align=ft.TextAlign.CENTER, border_color=ft.colors.DEEP_PURPLE_ACCENT_100, keyboard_type=ft.KeyboardType.NUMBER),
                ft.TextField(label="m", width=((page.width / 3) - 40), height=50, text_align=ft.TextAlign.CENTER, border_color=ft.colors.DEEP_PURPLE_ACCENT_100, keyboard_type=ft.KeyboardType.NUMBER),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e: remove_case(relation))
            ]
        )
        if len(relations_inputs) > 4:
                result_output.value = "Número de relações deve ser entre 2 e 5."
                page.update()
                return
        else:
            relations_inputs.append(relation)
            page.update()
    
    def remove_case(relation):
        relations_inputs.remove(relation)
        page.update()

    def solve_relations():
        try:
            if len(relations_inputs) < 2 or len(relations_inputs) > 4:
                result_output.value = "Número de relações deve ser entre 2 e 5."
                page.update()
                return
            
            a_values = []
            m_values = []
            for relation in relations_inputs:
                a = int(relation.controls[0].value)
                m = int(relation.controls[1].value)
                a_values.append(a)
                m_values.append(m)

            solution = chinese_remainder_theorem(a_values, m_values)
            result_output.value = f"Resultado: {solution}"
        except ValueError:
            result_output.value = "Entradas inválidas. Por favor, insira números inteiros."
        page.update()

    return ft.View(route="/sistema-de-congruencias", 
                controls=[
                    ft.AppBar(
                        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                        title=ft.Text("Sistema de Congruência"),
                        bgcolor=ft.colors.SURFACE_VARIANT
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Column(controls=relations_inputs),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.ElevatedButton(text="Adicionar Relação", on_click=lambda _: add_case()),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                    ft.ElevatedButton(text="Resolver", on_click=lambda _: solve_relations()),
                                ]
                            )
                        ]
                    ),
                    ft.Row(
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            result_output
                        ]
                    )
                ],
            )

def chinese_remainder_theorem(a, m):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        def mul_inv(a, b):
            gcd, x, _ = extended_gcd(a, b)
            if gcd == 1:
                return x % b
            return None

        def crt(a, n):
            sum = 0
            prod = reduce(lambda a, b: a*b, n)
            for ai, ni in zip(a, n):
                p = prod // ni
                sum += ai * mul_inv(p, ni) * p
            return sum % prod

        return crt(a, m)