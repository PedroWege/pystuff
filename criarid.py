# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:26:08 2020

Trial at an id making system for a Telegram Bot
i was making. The idea was to enable someking of game
to be played in a Telegram chatroom, so you could
count score and player history and stuff. With
id you could also challenge other players and keep
their wins, losses and stuff.

@author: PedroBoh
"""

from random import randint

debugmode = True

def string_gen(length):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    string=''
    for i in range(length):
        if randint(0,1) == 0: string = string+alfabeto[randint(0,25)]
        else: string = string+alfabeto[randint(0,25)].upper()
    return string

def open_player_ids():
    file = open('player_ids.txt','r')
    #opens player id file and writes it's contents to a list
    playerlist = file.readlines() 
    file.close()
    for i in range(len(playerlist)):#removes the line break \n text
        playerlist[i] = playerlist[i].replace('\n','')
    return playerlist

def validate_nick(playerlist,nick): #valida um nome escolhido, retorna string de erro se invalido ou True se for valido;
    validchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    buffer = nick.lower()
    listbuffer=[]
    for i in range(len(playerlist)):#gera uma lista minuscula baseada na lista original
        listbuffer.append(playerlist[i].lower())
    if buffer in listbuffer:#Verifica se o nome já está na lista
        if debugmode == True:
            print('Este nome de usuário já existe, tente novamente.')
        return 'Este nome de usuário já existe, tente novamente.'
    else: pass
    for i in buffer:
        if i in buffer: pass
        else:
            if debugmode == True:
                print('Este nome contém caracteres inválidos, tente novamente.')
            return 'Este nome contém caracteres inválidos, tente novamente.'
    else: return True

def player_add(playerlist,playername):#adiciona um player após validação por validate_nick()
    if validate_nick(playerlist,playername) == True:
        while True: #gera um codigo único e atribui ao nome do jogador
            if debugmode == True: codigo = 'teste'
            else:
                codigo = string_gen(5)
                try: #if this code already exists, try again until it's unique
                    playerdata = open('playerdata/'+codigo+'.txt','r')
                except:
                    break
        playerlist.append(playername+','+codigo+'\n')
        playerdata = open('playerdata/'+codigo+'.txt','w+')
        playerdata.write('0\n0')
        playerdata.close()
        if debugmode == True:
            print('Usuário '+playername+' criado, seu codigo é: '+codigo+'\nNão divida este codigo com ninguém!')
        return 'Usuário '+playername+' criado, seu codigo é: '+codigo+'\nNão divida este codigo com ninguém!'
    else: pass

def save_player_list(playerlist):
    currid = open('player_ids.txt','r')
    for i in range(len(playerlist)):
        currid.write(playerlist[i]+'\n')
    currid.close()

playerlist = open_player_ids()
print(playerlist)