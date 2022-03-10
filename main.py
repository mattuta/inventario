import PySimpleGUI as sg
import src.produto.cadastrar_produto as tela

sg.theme('Reddit')

layout = [
    [sg.Button('Cadastrar Produto')],
    [sg.Button('Adicionar Produto a Lista')]
          ]

window = sg.Window('Inventário', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    if event == 'Cadastrar Produto':
        tela.tela_cadastrar_produto()

    if event == 'Adicionar Produto a Lista':
        tela.tela_adicionar_produto()

window.close()