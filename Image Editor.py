import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

def update_image(original,blur,contrast,emboss,contour,flipx,flipy):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())
    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)
    


    bio = BytesIO()
    image.save(bio, format = 'PNG')

    window['-IMAGE-'].update(data = bio.getvalue())

image_path = '/Users/rrasmusson/Downloads/nail.png'

control_col = sg.Column([
    [sg.Frame('Blur',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-BLUR-')]])],
    [sg.Frame('Contrast',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-CONTRAST-')]])],
    [sg.Checkbox('Emboss',key = '-EMBOSS-'), sg.Checkbox('Contour',key = '-CONTOUR-')],
    [sg.Checkbox('Flip X',key = '-FLIPX-'), sg.Checkbox('Flip Y',key = '-FLIPY-')],
    [sg.Button('Save Image', key = '-SAVE-')],
])
image_col = sg.Column([[sg.Image(image_path, key = '-IMAGE-')]])
layout = [[control_col,image_col]]

original = Image.open(image_path)
window = sg.Window("Image Editor",layout, size=(715,350))

while True:
    event, values = window.read(timeout = 50)   
    if event == sg.WIN_CLOSED:
        break

    update_image(original,
        values['-BLUR-'],
        values['-CONTRAST-'],
        values['-EMBOSS-'],
        values['-CONTOUR-'],
        values['-FLIPX-'],
        values['-FLIPY-'])

    if event == '-SAVE-':
        save_path = sg.popup_get_file('Save', save_as = True, no_window = True) + '.png'
        image.save(save_path,'PNG')
window.close()