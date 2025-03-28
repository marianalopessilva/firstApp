import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


def main(page: ft.Page):
    # configuração da página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # definição de funções

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ],
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value= f'Bem vindo {input_nome.value}')
                    ],
                )
            )


        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)



    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    input_nome = ft.TextField(label="Digite seu nome:")

    page.go(page.route)





ft.app(main)