import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    # definição de funções
    def mostrar_idade(e):
        txt_resultado.value = input_data_de_nascimento.value
        data_de_nascimento = datetime.strptime(input_data_de_nascimento.value, "%d/%m/%Y")
        data_atual = datetime.now()
        idade = data_atual.year - data_de_nascimento.year


        if data_de_nascimento.month > data_atual.month:
            idade = idade - 1


        if int(idade) >= 18:
            txt_resultado.value = f'Tenho {idade} anos e sou maior de idade'
        else:
            txt_resultado.value = f'Tenho {idade} anos e sou menor de idade'
        page.update()
    # criação de componentes
    input_data_de_nascimento = ft.TextField(label="Data de Nascimento", hint_text="Digite sua data de nascimento")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_idade)
    txt_resultado = ft.Text(value="")
    # construir o layout
    page.add(
        ft.Column(
            [
                input_data_de_nascimento,
                btn_enviar,
                txt_resultado,
            ]
        )

    )


ft.app(main)