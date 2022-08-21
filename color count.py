# -*- coding: utf-8 -*-
"""
Counts the amount of pixels of each color in a sprite.
Very unoptimized, if you put a 1000x1000 colorful
image here. Prepare to wait and generate a horrible
useless output. Try with simple game sprites and it
should work fine.
Last tested years ago. Don't know if works. If not, test
pixel counter at github.com/PedroWege/pystuff/

@author: PedroBoh
"""

import PIL, random as rdm,sys,time, tkinter
from tkinter import filedialog as tkf

while True:
    break
    filname = str(input('Digite o nome da imagem com extensão, ex: image.png\n'))
    try:
        img = PIL.Image.open(filname)
        break
    except:
        print('Nome inválido, verifique se o arquivo existe e tente novamente.\n')
img = PIL.Image.open('x')
#Pega o valor de cada pixel de uma imagem e coloca em uma lista
def img_list(image):
    lista = []
    for i in range(image.height+1):
        for j in range(image.width+1):
            try:
                lista.append(image.getpixel((i,j)))
            except:
                pass
    return lista 

imgLista = img_list(img)

#Separa os quantos valores diferentes há em uma lista
#e conta quanto há de cada valor e coloca em
#um dicionario{valor:quantia}
def list_count(imgListaDummy):
    dicio = {}
    for i in range(len(imgListaDummy)):
        dicio[imgListaDummy[i]] = imgListaDummy.count(imgListaDummy[i])
        for j in range(imgListaDummy.count(i)):
            imgListaDummy.remove(imgListaDummy[i])
    return dicio

#Counts how many pixels of different colors there are in an image.
#Returns a dictionary: {Color:Pixel Count}
def pixel_count(image):
    lista = img_list(image)
    conta = list_count(lista)
    return conta
    
print(pixel_count(img))
