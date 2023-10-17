import PySimpleGUI as sg

menu_layout = [
    ['File',['Open','Save','---','Exit']]
    ]

title = 'Text Editor'
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline()]
    ]

window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        
window.close()