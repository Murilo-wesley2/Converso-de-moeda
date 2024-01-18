import requests
import keyboard
import PySimpleGUI as sg

def isfloat(valor):
    try:
        float(valor)
    except:
        return False
    else:
        return True
    

#Layout
sg.theme('Reddit')
layout=[
        [sg.Text('Real:'), sg.Input(key = 'real')],
        [sg.Text('Dolar:'), sg.Input(key = 'dolar')],
        [sg.Text('Euro:'), sg.Input(key = 'euro')],
        [sg.Text('Bitcoin:'), sg.Input(key = 'bitcoin')],
        [sg.Button('Converter'), sg.Button('Limpa')]
]

#Janela
janela=sg.Window('conversor de moeda',layout)

#Ler eventos
while True:
    try:
        requisicao=requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    
    except:
        break
    
    else:
        eventos, valores=janela.read()
        cotacao=requisicao.json()
        
        if eventos==sg.WINDOW_CLOSED:
            break
        if eventos == 'Converter' or keyboard.is_pressed('enter'):
            if valores['real'] == '' and valores['euro'] == '' and valores['bitcoin'] == '' and valores['dolar'] == '':
                if valores['real']=='':
                    valores['real']='0'
            
            if isfloat(valores['real']):
                eur = float(valores['real'])/float(cotacao['EURBRL']['bid'])
                janela['euro'].update(str(f'{eur:.2f}'))

                usd = float(valores['real'])/float(cotacao['USDBRL']['bid'])
                janela['dolar'].update(str(f'{usd:.2f}'))

                bitc = float(valores['real'])/float(cotacao['BTCBRL']['bid'])
                janela['bitcoin'].update(str(f'{bitc:.2f}'))
            
            elif isfloat(valores['euro']):
                brl = float(valores['euro'])*float(cotacao['EURBRL']['bid'])
                janela['real'].update(str(f'{brl:.2f}'))

                usd = float(valores['euro'])*(float(cotacao['EURBRL']['bid'])/float(cotacao['USDBRL']['bid']))
                janela['dolar'].update(str(f'{usd:.2f}'))

                bitc = float(valores['euro'])*(float(cotacao['EURBRL']['bid'])/float(cotacao['BTCBRL']['bid']))
                janela['bitcoin'].update(str(f'{bitc:.2f}'))
            
            elif isfloat(valores['bitcoin']):
                brl = float(valores['bitcoin'])*float(cotacao['BTCBRL']['bid'])
                janela['real'].update(str(f'{brl:.2f}'))

                usd = float(valores['bitcoin'])*(float(cotacao['BTCBRL']['bid'])/float(cotacao['USDBRL']['bid']))
                janela['dolar'].update(str(f'{usd:.2f}'))

                eur = float(valores['bitcoin'])*(float(cotacao['BTCBRL']['bid'])/float(cotacao['EURBRL']['bid']))
                janela['euro'].update(str(f'{eur:.2f}'))
            
            elif isfloat(valores['dolar']):
                brl = float(valores['dolar'])*float(cotacao['USDBRL']['bid'])
                janela['real'].update(str(f'{brl:.2f}'))

                bitc = float(valores['dolar'])*(float(cotacao['USDBRL']['bid'])/float(cotacao['BTCBRL']['bid']))
                janela['bitcoin'].update(str(f'{bitc:.2f}'))

                eur = float(valores['dolar'])*(float(cotacao['USDBRL']['bid'])/float(cotacao['EURBRL']['bid']))
                janela['euro'].update(str(f'{eur:.2f}'))
        if eventos == 'Limpa':
            for valor in ('real','euro','bitcoin','dolar'):
                janela[valor].update('')