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
def number():
    global n
    while True :
        n_ch = raw_input("Choisis le numero : ")
        try:
            n=int(n_ch)
        except:
            continue
        if n in range(50) :
            break

#Read the bet
def bet():
    global m
    while True :
        m_ch = raw_input("Misez en dollars : ")
        try:
            m=int(m_ch)
        except:
            continue
        if m<=Argent :
            break
#Again ?
def again():
    r ='0'
    while r not in ['Y','N','y','n'] :
        r=raw_input("Replay? Y/N :")
    if r == 'Y' or r == 'y' :
        return True
    return False

    

#PP
Argent = 1000
number()
while True :
    w = randrange(50)
    bet()
    print 'Le numero gagnant est : ', str(w)
    if w == n :
        m *=3
        print 'Vous avez gagnez ! ' + str(m) +'$'
        Argent = Argent + m
        print '*****Money : {}$*****'.format(Argent)
    elif isOdd(w,n):
         m = ceil(m/2)
         print 'Vous avez perdu la moitié de votre mise ' + str(m)
         Argent = Argent - m
         print '*****Money : {}$*****'.format(Argent)
    else :
        print 'Desole vous avez perdu {}'.format(m)
        Argent = Argent - m
        print '*****Money : {}$*****'.format(Argent)
    
    
    if Argent == 0 : 
        break
    test = again()
    if test :
        print 'YES'
        continue
    else:
        print 'NO'
        break
print 'Thank you for playing ZCasino'
if Argent > 1000 :
    w = Argent - 1000
    print 'Vous avez gagnez en tatal {}$'.format(w)
elif Argent < 1000 :
    w = 1000 - Argent
    print 'Vous avez perdu en tatal {}$'.format(w)
else:
    print "Tu n'as rien perdu n'i gagner "
    
    


    
    


    

    
