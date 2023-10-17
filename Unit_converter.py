import PySimpleGUI as sg

title = 'Unit Converter'
layout = [
    [sg.Input(key = '-INPUT-'),sg.Spin(['km to mile', 'kg to pound', 'Celsius to Farenheit'],key = '-UNITS-'),sg.Button('convert',key = '-CONVERT-')],
    [sg.Text('output',key = '-OUTPUT-')]]

window = sg.Window(title,layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_str = f'{input_value} km is {output} miles.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462,2)
                    output_str = f'{input_value} kg is {output} pounds.'
                case 'Celsius to Farenheit':
                    output = round(((9/5)*(float(input_value)) + 32),2)
                    output_str = f'{input_value} degrees Celcius is {output} degrees Farenheit.'
            window['-OUTPUT-'].update(output_str)
        else:
            window['-OUTPUT-'].update('Please enter a number')
        
window.close()