from datetime import datetime

import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


def main(page: ft.Page):
    # configuração da página
    page.title = "Simulador de aposentadoria"
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
                    AppBar(title=Text("Olá, seja bem-vindo ao INSS"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Simular aposentadoria", on_click=lambda _: page.go("/segunda")),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/terceira")),
                ],
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'Simule sua aposentadoria:'),
                        input_idade,
                        menu,
                        input_contribuicao,
                        input_media_salarial,
                        categoria,
                        ElevatedButton(text="Simular aposentadoria", on_click=lambda _: page.go("/quarta")),
                    ],
                )
            )

        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Terceira tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'Regras da aposentadoria'),
                        Text(value=f'Aposentadoria por Idade:'),
                        Text(value=f'Homens: 65 anos de idade e pelo menos 15 anos de contribuição.'),
                        Text(value=f'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.'),
                        Text(value=f'Aposentadoria por Tempo de Contribuição:'),
                        Text(value=f'Homens: 35 anos de contribuição. '),
                        Text(value=f'Mulheres: 30 anos de contribuição. '),
                        Text(value=f'Valor Estimado do Benefício:'
                                   f' O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                   f' acrescido de 2% por ano que exceder o tempo mínimo de contribuição.'),
                    ],
                )
            )

        if page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        AppBar(title=Text("Quarta tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f''),
                        genero(e),
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
    input_idade = ft.TextField(label="Digite sua idade:")
    menu = ft.Dropdown(
        label="Menu",
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Feminino")]
    )
    input_contribuicao = ft.TextField(label="Digite seu tempo de contribuição com o INSS:")
    input_media_salarial = ft.TextField(label="Digite sua média salarial dos últimos 5 anos de contribuição:")
    categoria = ft.Dropdown(
        label="Menu",
        options=[Option(key="Contribuicao", text="Por tempo de contribuição"), Option(key="Idade", text="Por idade")]
    )

    def genero(e):
        if categoria.value == "Idade":
            if menu.value == "Fem":
                if int(input_idade.value) >= 62 and input_contribuicao.value == 15:
                    aposentadoria_i = float(input_media_salarial.value) * 0.6
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_i}'

                elif int(input_idade.value) >= 62 and int(input_contribuicao.value) > 15:
                    aposentadoria_tc = float(input_media_salarial.value) * 0.6
                    diferenca = float(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    aposentadoria_tc_total = aposentadoria_tc + extra
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_tc_total}'

                else:
                    ano_atual = datetime.now().year
                    data_da_aposentadoria = (int(input_idade.value) - 62) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas, poderá em {data_da_aposentadoria}'

            else:
                if int(input_idade.value) >= 65 and int(input_contribuicao.value) == 15:
                    aposentadoria_i = float(input_media_salarial.value) * 0.6
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_i}'

                elif int(input_idade.value) >= 65 and int(input_contribuicao.value) > 15:
                    aposentadoria_c = float(input_media_salarial.value) * 0.6
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    aposentadoria_c_total = aposentadoria_c + extra
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_c_total}'

                else:
                    ano_atual = datetime.now().year
                    data_da_aposentadoria = (int(input_idade.value) - 65) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas, poderá em {data_da_aposentadoria}'

        else:
            if menu.value == "Fem":
                if int(input_contribuicao.value) == 30:
                    aposentadoria_tc = float(input_media_salarial.value) * 0.6
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_tc}'

                elif int(input_contribuicao.value) > 30:
                    aposentadoria_tc = float(input_media_salarial.value) * 0.6
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    aposentadoria_tc_total = aposentadoria_tc + extra
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_tc_total}'

                else:
                    ano_atual = datetime.now().year
                    data_da_aposentadoria = (int(input_contribuicao.value) - 30) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas, poderá em {data_da_aposentadoria}'

            else:
                if int(input_contribuicao.value) == 35:
                    aposentadoria_tc = float(input_media_salarial.value) * 0.6
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_tc}'

                elif int(input_contribuicao.value) > 35:
                    aposentadoria_tc = float(input_media_salarial.value) * 0.6
                    diferenca = int(input_contribuicao.value) - 15
                    extra = diferenca * 0.2
                    aposentadoria_tc_total = aposentadoria_tc + extra
                    Text.value = f'Você pode se aposentar e sua aposentadoria será de R${aposentadoria_tc_total}'

                else:
                    ano_atual = datetime.now().year
                    data_da_aposentadoria = (int(input_contribuicao.value) - 35) + ano_atual
                    Text.value = f'Você ainda não pode se aposentar, mas, poderá em {data_da_aposentadoria}'

    page.go(page.route)


ft.app(main)
