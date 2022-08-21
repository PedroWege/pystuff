# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:20:03 2020

Counts the amount of pixels of each color in a sprite.
Very unoptimized, if you put a 1000x1000 colorful
image here. Prepare to wait and generate a horrible
useless output. Try with simple game sprites and it
should work fine.
Last tested years ago. Don't know if works.

@author: PedroBoh
"""

import tkinter, sys
#import random as rdm,sys,time
from tkinter import filedialog as tkf
from PIL import Image,ImageDraw,ImageFont

#    Open an image file.

debugmode = False
def open_image():
    if debugmode == True:
        imagevar = Image.open("1024.png")  
    else:
        tk = tkinter.Tk()
        tk.withdraw()
        file_path = tkf.askopenfilename()
        print(file_path)
        imagevar = Image.open(file_path)
        tk.destroy
    imagevar.convert("RGB")    
    return imagevar

#   Turn an image into a list.
def img_list(image):
    lista = []
    for i in range(image.height+1):
        for j in range(image.width+1):
            try:
                lista.append(image.getpixel((i,j)))
            except:
                pass
    return lista 

#   Count how many of each value there is in a list.
def list_count(imgListaDummy):
    dicio = {}
    for i in range(len(imgListaDummy)):
        dicio[imgListaDummy[i]] = imgListaDummy.count(imgListaDummy[i])
        for j in range(imgListaDummy.count(i)):
            imgListaDummy.remove(imgListaDummy[i])
    return dicio

#   Turns an image into a list, then count how many pixels of each color there are.
def pixel_count(image):
    lista = img_list(image)
    conta = list_count(lista)
    return conta

# Code references
# output = Image.new("RGB",(100,100),(255,0,0))
# output2 = Image.new("RGB",(100,100),(255,255,0))
# output3 = Image.new("RGB",(output.height+output2.height,output.width),(0,0,0))
# output3.paste(output,(0,0))
# output3.paste((output2),(output.width,0))
# draw = ImageDraw.Draw(output3)
# fonte = ImageFont.truetype("calibri.ttf",20)
# draw.text((25,25),"Teste",font=fonte,fill=(0,0,0))


#Counts the pixel colors in an image then puts in a dictionary
img = open_image()
conta = pixel_count(img)

#determine screen width based on imagewidth or horizontal text, which is bigger
if img.width >= 100:
    screenwidth = img.width
else:
    screenwidth = 100

#determine screen height based on image height and number of colors
screenheigth = img.height+30+(len(conta)*22+20)
screensize = (screenwidth,screenheigth) 


#Create a canvas to draw the final info onto.
screenbg = Image.new("RGB",screensize,(0,255,0))


#Draw the loaded image first on top
screenbg.paste(img,(round((screenwidth-img.width)/2),10))
#makes a list with a square image in each index for each color.
colorList = []
contaIndex = list(conta)
for i in range(len(contaIndex)):
    colorList.append(Image.new("RGB",(20,20),contaIndex[i]))

fonte = ImageFont.truetype("calibri.ttf",20)
texto = ImageDraw.Draw(screenbg)
#texto.text((50,50),"teste",font=fonte,fill=(0,0,0))
for i in range(len(conta)):
    texto.text((50,img.height+40+(i*22)),str(conta.get(contaIndex[i])),fill=(0,0,0))
    screenbg.paste(colorList[i],(20,img.height+35+(i*22)))
    
screenbg.show()

sys.exit()
# draw.text((25,25),"Teste",font=fonte,fill=(0,0,0))
