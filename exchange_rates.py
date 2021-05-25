import PySimpleGUI as sg
import requests


response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
print(response.json())
def get_buy(obj):
  return obj.get('buy')

def get_sell(obj):
  return obj.get('sale')


sg.theme('dark green 3')
layout = [[sg.Text('КУРС К ГРИВНЕ', size=(25, 1), background_color=sg.theme_background_color()), sg.Text('Покупка', size=(15, 1)), sg.Text('Продажа', size=(15, 1))],
          [sg.Text('Доллар', size=(25, 1), background_color=sg.theme_background_color()), sg.Text(get_buy(response.json()[0]), size=(15, 1), key='-usd_buy-'), sg.Text(get_sell(response.json()[0]), size=(15, 1), key='-usd_sell-')],
          [sg.Text('ЕВРО', size=(25, 1), background_color=sg.theme_background_color()), sg.Text(get_buy(response.json()[1]), size=(15, 1), key='-eur_buy-'), sg.Text(get_sell(response.json()[1]), size=(15, 1), key='-eur_sell-')],
          [sg.Text('РУБЛЬ', size=(25, 1), background_color=sg.theme_background_color()), sg.Text(get_buy(response.json()[2]), size=(15, 1), key='-rub_buy-'), sg.Text(get_sell(response.json()[2]), size=(15, 1), key='-rub_sell-')],
          [sg.Button('Обновить', key='-UPDATE-')]]


def get_json_usd(obj, window):
  window.FindElement('-usd_buy-').Update(get_buy(obj))
  window.FindElement('-usd_sell-').Update(get_sell(obj))


def get_json_euro(obj, window):
  window.FindElement('-eur_buy-').Update(get_buy(obj))
  window.FindElement('-eur_sell-').Update(get_sell(obj))


def get_json_rub(obj, window):
  window.FindElement('-rub_buy-').Update(get_buy(obj))
  window.FindElement('-rub_sell-').Update(get_sell(obj))
    

window = sg.Window('Курс валют - Приват Банк', layout, use_custom_titlebar=True)
if response.status_code == 200:
  while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Выход'):
      break
    if event == '-UPDATE-':
      get_json_usd(response.json()[0], window)
      get_json_euro(response.json()[1], window)
      get_json_rub(response.json()[2], window)

  window.close()
