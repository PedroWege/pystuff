'''
Author: PedroBoh

Rola um dado como preferir e usa efeitinhos maneiros
de printar texto por tempo.
'''
import sys, time, random

def prinText(text,spd=None):
    text=str(text)
    if spd is None:
        spd = 20
    else:
        pass
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(spd/1000)
        
def dadoRoll(maxRoll,minRoll=1):
  
    dado = random.randint(minRoll,maxRoll)
    prinText('Dado = '+str(dado))
    
esco=0

while True:
      
    while True:
        try:
            prinText('\nEscolha: \n(1)D6, (2)D10, (3)D20, (4)Personalizado ou (5)Sair')
            esco= int(input('\n'))
            break
            
        except:
            prinText('\nEscolha inválida.')
    
    if esco == 1:
        dadoRoll(6)
        
    elif esco == 2:
        dadoRoll(10)
        
    elif esco == 3:
        dadoRoll(20)
        
    elif esco == 4:
        while True:
            prinText('\nDigite o valor mínimo.')
            try:
                dmin=int(input('\n'))
                break
            except:
                prinText('\nValor inválido.')
                
        while True:
            prinText('\nDigite o valor máximo.')
            try:
                dmax=int(input('\n'))
                if dmax < dmin:
                    prinText('\nValor maximo deve ser maior que o mínimo.')
                else:
                    break
            except:
                prinText('\nValor inválido.')
            

        dadoRoll(dmax,dmin)
        
    elif esco == 5:
        exit()
    
    
    else:
        prinText('\nEscolha inválida')
