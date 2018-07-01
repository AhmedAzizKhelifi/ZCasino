# -*- coding: cp1252 -*-
#ZCasino
from random import randrange
from math import ceil

def isOdd(a,b):
    if a % 2 == 0 :
        if b % 2 == 0 :
            return True
        else:
            return False
    if a%2 != 0:
        if b%2!=0:
            return True
        else :
            return False


#Read the player number.
while True :
    n_ch = raw_input("Choisis le numero : ")
    try:
        n=int(n_ch)
    except:
        continue
    if n in range(50) :
        break
#Read the bet
while True :
    m_ch = raw_input("Misez en dollars : ")
    try:
        m=int(m_ch)
    except:
        continue
    if m>0 :
        break

w = randrange(50)
print 'Le numero gagnant est : ', w
if w == n :
    m *=3
    print 'Vous avez gagnez ! ' + str(m) +'$'
elif isOdd(w,n):
    print 'Vous avez perdu la moitié de voitre mise :( '
    m = ceil(m/2)
    print 'Vous avez : ' + str(m) + '$'
else :
    print 'Desole vous avez perdu :( '
    


    

    
