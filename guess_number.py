import PySimpleGUI as sg
import random

'''
    App that shows "how fonts work in PySimpleGUI".
'''

number = random.randint(1, 10)
count = 3
attempt = 0

layout = [[sg.Text('Привет, я загадал число от 1 до 10!', size=(60, 1), key='-text-')],
          [sg.Text('Попробуешь угадать?', size=(60, 1), key='-text2-')],
          [sg.Text('Попыток: 3', size=(30, 1), key='-attempt_text-')],
          [sg.Radio('1', 'number', key='1', change_submits=True),
           sg.Radio('2', 'number', key='2', change_submits=True),
           sg.Radio('3', 'number', key='3', change_submits=True),
           sg.Radio('4', 'number', key='4', change_submits=True),
           sg.Radio('5', 'number', key='5', change_submits=True),
           sg.Radio('6', 'number', key='6', change_submits=True),
           sg.Radio('7', 'number', key='7', change_submits=True),
           sg.Radio('8', 'number', key='8', change_submits=True),
           sg.Radio('9', 'number', key='9', change_submits=True),
           sg.Radio('10', 'number', key='10', change_submits=True),],
          [sg.Button('Выход'), sg.Button('Обновить', key='-UPDATE-',)]]

def update(window, sg):
    global count
    global number
    global attempt
    
    number = random.randint(1, 10)
    count = 3
    attempt = 0
    
    for i in range(1, 11):
        window.FindElement(str(i)).Update(background_color=sg.theme_background_color(),)
        
    window['-attempt_text-'].update("Попыток: {}".format(count))
    window['-text-'].update('Привет, я загадал число от 1 до 10!')
    window['-text2-'].update('Попробуешь угадать?')

# Update function
def start(num):
    global count
    global number
    global attempt
    
    attempt += 1    
    
    user_number = num
    window.FindElement(str(num)).Update(background_color='red',)
    if user_number < number:
        window['-text-'].update("Твое число меньше того, что я загадал!")
        window['-text2-'].update("Попробуй еще!")
    elif user_number > number:
        window['-text-'].update("Твое число больше того, что я загадал!")
        window['-text2-'].update("Попробуй еще!")
    else:
        window['-text-'].update("Ты угадал! Тебе понадобилось попыток: {}".format(attempt))
        window.FindElement(str(num)).Update(background_color='green',)
        window['-text2-'].update("Сыграем еще разок? Нажми кнопку 'Обновить'")
        
    count -= 1
    
    window['-attempt_text-'].update("Попыток: {}".format(count))
    if count > 0:
        pass
    elif user_number == number:
        pass
    else:
        window['-attempt_text-'].update("Попыток: {}".format(count))
        window['-text-'].update("Ты не угадал( Мое число было {}".format(number))
        window['-text2-'].update("Сыграем еще разок? Нажми кнопку 'Обновить'!")
        

sg.theme('dark blue 14')
window = sg.Window('Угадай число', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Выход'):
        break
    if event == '-UPDATE-':
        update(window, sg)
    elif event:
        start(int(event))
        

window.close()