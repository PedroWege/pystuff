"""
Aparador de CNPJ por Pedro Chagas
pedrowchagas@gmail.com

Changelog:
27/05/22 - 1.01:
    Error state added.
10/05/22 - 1.0
"""

from pyperclip import copy as copy
from time import sleep as sleep

while True:
    entrada = str(input('Cole o CNPJ a converter ou digite "Sair" para encerrar\n'))
    if entrada.lower() == 'sair':
        break

    allowed = '' #números permitidos
    saida = '' #valor a ser colado na área de transferência
    for i in range(10): #determina os números permitidos
        allowed = allowed + str(i)
        
    for i in range(len(entrada)): #passa por todos os números da entrada
        if entrada[i] in allowed: #filtra só os números permitidos e cola na saida
         saida = saida + entrada[i]
         
    if saida=="":
        print('Erro, é necessário haver números, tente de novo.')
    else:
        try: 
            copy(saida)
            print(saida+ ' colado na área de transferência.')
        except:
            print('erro')
    
    sleep(1)
    print('')
