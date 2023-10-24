import requests
import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout=[
        [sg.Text('Real'),sg.Input(key='real')],
        [sg.Button('Converte')],
        [sg.Output(size=(10,3),key='saida')]
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
        if eventos=='Converte':
            valor=float(valores['real'])/float(cotacao['USDBRL']['bid'])
            print(f'{valor:.2f}')
