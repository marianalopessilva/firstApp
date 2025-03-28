import flet as ft


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # definição de funções
    def par_ou_impar(e):
        txt_resultado.value = input_numero.value
        numero = int(input_numero.value)
        resultado = numero % 2
        if resultado == 0:
            txt_resultado.value = f'Par'
        else:
            txt_resultado.value = f'Impar'
        page.update()

    # criação de componentes
    input_numero = ft.TextField(label="Número", hint_text="Digite um número")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=par_ou_impar,
    )
    txt_resultado = ft.Text(value="")
    # construir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]
        )

    )


ft.app(main)