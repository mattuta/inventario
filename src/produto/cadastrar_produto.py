import PySimpleGUI as sg


def tela_cadastrar_produto():
    sg.theme('Reddit')

    layout = [[sg.Text('Cadastrar Produto')],
              [sg.Text('Descrição'), sg.InputText()],
              [sg.Text('Marca'), sg.InputText()],
              [sg.Button('Salvar'), sg.Button('Cancelar')]]

    window = sg.Window('Cadastrar Produto', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        print('Teste', values[0])

    window.close()
