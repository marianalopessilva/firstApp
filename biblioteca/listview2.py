import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.types import CrossAxisAlignment
from models import Usuario, db_session
from sqlalchemy import select


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    def salvar_nome(e):
        if input_nome.value == "" or input_profissao.value == "" or input_salario.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = Usuario(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=float(input_salario.value),
            )
            obj_user.save()
            input_nome.value = ""
            input_profissao.value = ""
            input_salario.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()



    def exibir_lista(e):
        lv_nome.controls.clear()
        user = select(Usuario)
        usuarios = db_session.execute(user).scalars().all()
        for u in usuarios:
            lv_nome.controls.append(
                ft.Text(value=f"{u.nome} - {u.profissao} - {u.salario}"),
            )

        page.update()


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    ft.Container(
                        ft.Image(src='users.jpg', width=300, height=200),
                    ),
                    AppBar(title=Text(""), bgcolor=Colors.BLACK),
                    input_nome,
                    input_profissao,
                    input_salario,
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
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text(""), bgcolor=Colors.BLACK),
                        lv_nome,

                    ],
                    bgcolor=Colors.BLACK,
                )
            )
        page.update()


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
        content=ft.Text("Nenhum campo pode ser vazio!"),
        bgcolor=Colors.RED
    )
    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissao")
    input_salario = ft.TextField(label="Salário")


    lv_nome = ft.ListView(
        height=500
    )


    # Eventos
    page.on_route_change = gerencia_rotas
    # page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)