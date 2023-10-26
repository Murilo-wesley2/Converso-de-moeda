import requests
import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout=[
        [sg.Text('Real'),sg.Input(key='real')],
        [sg.Button('USD'), sg.Button('EUR'), sg.Button('BTC')],
        [sg.Text('',key='saida')]
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
        
        if valores['real']=='':
            valores['real']='0'
        if eventos==sg.WINDOW_CLOSED:
            break
        if valores['real'].isnumeric()==True:
            if eventos=='USD':
                moeda='USDBRL'
                simbolo='US$'
            elif eventos=='EUR':
                moeda='EURBRL'
                simbolo='€'
            elif eventos=='BTC':
                moeda='BTCBRL'
                simbolo='₿'
            valor=float(valores['real'])/float(cotacao[moeda]['bid'])
            janela['saida'].update(f'{simbolo} {valor:.2f}')
        else:
            janela['saida'].update('digite apenas numeros')
