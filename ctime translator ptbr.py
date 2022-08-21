# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:31 2020

Traduz saidas da função ctime de inglês para português.

@author: PedroBoh
"""
from time import ctime
from time import time
#'Sun Apr 26 15:54:57 2020' ctime generic structure
def ctime_translate_ptbr(timestring):#timestring needs to have ctime() structure
    weekday = (timestring[0]+timestring[1]+timestring[2])
    month = (timestring[4]+timestring[5]+timestring[6])
    day = (timestring[8]+timestring[9])
    houryear=''
    for i in range(len(timestring)-11):
        houryear = houryear+timestring[i+11]
    
    meses = {
        'Jan':'Jan',
        'Feb':'Fev',
        'Mar':'Mar',
        'Apr':'Abr',
        'May':'Mai',
        'Jun':'Jun',
        'Jul':'Jul',
        'Aug':'Ago',
        'Sep':'Set',
        'Oct':'Out',
        'Nov':'Nov',
        'Dec':'Dez'
        }
    diasemana = {
        'Mon':'Seg',
        'Tue':'Ter',
        'Wed':'Qua',
        'Thu':'Qui',
        'Fri':'Sex',
        'Sat':'Sab',
        'Sun':'Dom'
        }
    dataTradu = diasemana[weekday]+' '+day+' '+meses[month]+' '+houryear
    print(dataTradu)
    
ctime_translate_ptbr(ctime())

'''ctime structure:
    Months:
Sun Apr 26 16:24:32 2020
Fri Mar 27 16:24:32 2020
Wed Feb 26 16:24:32 2020
Mon Jan 27 16:24:32 2020
Sat Dec 28 16:24:32 2019
Thu Nov 28 16:24:32 2019
Tue Oct 29 16:24:32 2019
Sun Sep 29 16:24:32 2019
Fri Aug 30 16:24:32 2019
Wed Jul 31 16:24:32 2019
Mon Jul  1 16:24:32 2019
Sat Jun  1 16:24:32 2019
Thu May  2 16:24:32 2019
Tue Apr  2 16:24:32 2019

    Weekdays:
Sun Apr 26 16:25:25 2020
Sat Apr 25 16:25:25 2020
Fri Apr 24 16:25:25 2020
Thu Apr 23 16:25:25 2020
Wed Apr 22 16:25:25 2020
Tue Apr 21 16:25:25 2020
Mon Apr 20 16:25:26 2020
Sun Apr 19 16:25:26 2020'''