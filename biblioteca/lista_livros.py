import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.types import CrossAxisAlignment


class livro():
    def __init__(self, titulo, descricao, categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor


def main(page: ft.Page):
    # Configurações
    page.title = "Lista de Livros"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_nome(e):
        if input_titulo.value == "" or input_descricao.value == "" or input_categoria.value == "" or input_autor.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_livro = livro(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value,
            )
            lista.append(obj_livro)
            input_titulo.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()



    def exibir_lista(e):
        lv_livros.controls.clear()
        for livro in lista:
            lv_livros.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Titulo - {livro.titulo}"),
                    subtitle=ft.Text(f"Sub titulo - {livro.autor}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem("Detalhes")
                        ],
                        on_select=lambda _: exibir_detalhes(livro.titulo, livro.autor, livro.descricao, livro.categoria),
                    )
                )
            )

        page.update()


    def exibir_detalhes(titulo, autor, descricao, categoria):
        txt_titulo.value = titulo
        txt_autor.value = autor
        txt_descricao.value = descricao
        txt_categoria.value = categoria

        page.go("/terceira")



    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    ft.Container(
                        ft.Image(src='livros.jpg', width=300, height=200),
                    ),
                    AppBar(bgcolor=Colors.BLACK),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        text="Salvar",
                        color=Colors.WHITE,
                        on_click=lambda _: salvar_nome(e)
                    ),
                    ft.Button(
                        text="Exibir Lista",
                        color=Colors.WHITE,
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
                bgcolor=ft.Colors.BLACK,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        if page.route == "/segunda" or page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text(""), bgcolor=Colors.BLACK),
                        lv_livros,

                    ],
                    bgcolor=ft.Colors.BLACK,
                )
            )
        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text(""), bgcolor=Colors.BLACK),
                        txt_titulo,
                        txt_autor,
                        txt_descricao,
                        txt_categoria,
                    ],
                    bgcolor=ft.Colors.BLACK,
                )
            )

        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
        content=ft.Text("Nenhum campo pode ser vazio!"),
        bgcolor=Colors.RED
    )
    input_titulo = ft.TextField(label="Título do livro:", multiline=True)
    input_descricao = ft.TextField(label="Descrição do livro:", multiline=True)
    input_categoria = ft.TextField(label="Categoria do livro:", multiline=True)
    input_autor = ft.TextField(label="Autor do livro:", multiline=True)


    txt_titulo = ft.Text(value="")
    txt_autor = ft.Text(value="")
    txt_descricao = ft.Text(value="")
    txt_categoria = ft.Text(value="")


    lv_livros= ft.ListView(
        height=500
    )


    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)