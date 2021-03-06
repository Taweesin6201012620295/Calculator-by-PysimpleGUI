### This not complete , DEL can't use , Number far for length
### update 10/09/2020

import PySimpleGUI as sg 

sg.theme('DarkBlack')
bw: dict = {'size':(7,2),'font':('Franklin Gothic Book', 24)}
bt: dict = {'size':(7,2),'font':('Franklin Gothic Book', 24)}
bo: dict = {'size':(15,2),'font':('Franklin Gothic Book', 24), 'focus':True}

##Window and Layout##
layout: list = [
    [sg.Text('0.0000', size=(24,2), justification='right', background_color='black', text_color='blue', font=('Franklin Gothic Book',45), relief='sunken', key="_DISPLAY_")],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("DEL",**bt),sg.Button("AC",**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("*",**bt),sg.Button('/',**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt),sg.Button('-',**bt)],    
    [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo, bind_return_key=True),sg.Button('%',**bt)]
]

window: object = sg.Window('Calculator', layout=layout, background_color="#000000", size=(700, 620), return_keyboard_events=True)
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

##############################################################################

def format_number():
    ''' Create a consolidated string of numbers from front and back lists '''
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def update_display(display_value: str):
    ''' Update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

def number_click(event: str):
    ''' Number button button click event '''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())
    
def clear_click():
    ''' AC button click event '''
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 

def operator_click(event: str):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()

def calculate_click():
    ''' Equals button click event '''
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()    
    except:
        update_display("SYSNTEX ERROR")
        clear_click()

###############################################

while True:
    event, values = window.read()

    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['AC']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)