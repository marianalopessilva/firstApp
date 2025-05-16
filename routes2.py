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
                    AppBar(title=Text("Cadastre seu livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
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
                        Text(value= f'Título do livro: {input_titulo.value}'),
                        Text(value= f'Descrição do livro: {input_descricao.value}'),
                        Text(value= f'Categoria do livro: {input_categoria.value}'),
                        Text(value= f'Autor do livro: {input_titulo.value}'),
                    ],
                )
            )


        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    input_titulo = ft.TextField(label="Título do livro:", multiline=True)
    input_descricao = ft.TextField(label="Descrição do livro:", multiline=True)
    input_categoria = ft.TextField(label="Categoria do livro:", multiline=True)
    input_autor = ft.TextField(label="Autor do livro:", multiline=True)


    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)



ft.app(main)