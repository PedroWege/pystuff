# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:58:47 2021

@author: PedroBoh
"""

from random import randint
from time import time
from time import sleep
import sys

def contador():
    global timer
    return round(time()-timer)

debugCounter = 0

def entrada(tipo,texto,erro,string = ['']): #tipo de valor, mensagem, mensagem de erro

    if tipo == 'int': #Qual tipo de valor será retornado
        while True: #permite tentar denovo caso o valor colocado seja inválido
            try:
                saida = int(input(texto))
                if saida < 0:
                    print(erro)
                    input('Pressione Enter para continuar.\n')
                else: break
            except:
                print(erro)
                input('Pressione Enter para continuar.\n')
    
    if tipo == 'str': #Qual tipo de valor será retornado
        loop = True
        while loop == True: #permite tentar denovo caso o valor colocado seja inválido
            try:
                saida = input(texto)
                saida = str(saida)
                for i in range(len(string)):
                    if saida.lower() == string[i]:
                        saida = i + 1
                        loop = False
                        break
                    else: pass
                break
            except:
                break
    #elif
    
    return saida


print('''Este script rola um dado baseado nos valores que inserir. Toda vez 
      que o valor maximo for rolado, o contador de vitorias subirá, caso caia 
      outro valor, o contador voltará a 0. O programa termina quando conseguir 
      o número de vitorias seguidas que for inserido.''')

while True:
    
          
    #minimo = entrada('int','Insira um valor mínimo.\n','Apenas números inteiros.')
    minimo = 1
    maximo = entrada('int','Insira um valor máximo.\n','Apenas números inteiros.')
    #maximo = 10
    #tentativas = 6
    tentativas = entrada('int','Quantas vitorias consecutivas?\n','Apenas números inteiros.')
    
    estimativa = (maximo-minimo+1)**tentativas
    print('Quantidade média de tentativas necessárias: '+str(round(estimativa)))
    
    update = entrada('int','Quantas tentativas * 1000 por atualização de status? (Recomenda-se a partir de 1 milhão)\n','Apenas números inteiros.')
    #update = 1000
    update *= 1000    
    contagem = 0
    timer = time()
    atual = 0
    dado = 0
    
    print('')
    
    #roda o script normalmente rolando o dado tentando atingir vitorias consecutivas
    #e usa este período para estimar a demora para o termino do script usando
    #o número de ciclos rodados em 1 segundo
    while True:
        dado = randint(minimo, maximo)
        #print(str(dado))
        #sleep(0.1)
        contagem += 1
        if dado == maximo:
            atual += 1
        else: atual = 0
        if time()-timer > 1:
            print('Tentativas em 1 segundo: '+str(contagem))
            print('Estimativa de tempo para concluir: '+str(round((time()-timer)*(estimativa/contagem)))+' segundos.')
            break
        if atual == tentativas:
            break
    print('')
    
    #ao passar 1 segundo, segue com um script igual mas sem checar se passou 1 segundo
    #a cada tantos segundos irá dizer quantas tentativas foram feitas e outros status
    if time()-timer > 1 and atual < tentativas:
        while True:
            dado = randint(minimo,maximo)
            #print(str(dado)+'pos 1 segundo')
            #sleep(0.1)
            contagem += 1
            if dado == maximo:
                atual += 1
            else: atual = 0
            if update != 0: #Caso o valor escolhido for 0, não faz atualizações.
                if contagem % update == 0:
                    print(str(contagem)+' tentativas realizadas.')
                    print(str(contador())+' segundos passados.')
            if atual == tentativas:
                break
    print('')
    #else: 
    print(str(tentativas)+' vitorias atingidas em '+str(contador())+' segundos.')
    print(str(contagem)+' tentativas realizadas.')
    encerrar = entrada('str','Para sair digite sair, ou qualquer coisa para continuar\n','''
                       'Opção inválida.\n''',['sair'])
    print (str(encerrar))
    if encerrar == 1:
        break
    else: pass