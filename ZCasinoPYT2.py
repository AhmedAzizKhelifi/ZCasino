# -*- coding: cp1252 -*-
#ZCasino
from random import randrange
from math import ceil
import os

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
print("""La roulette est constitu�e de 50 cases allant de 0 � 49. Les num�ros pairs sont de couleur noire, les num�ros impairs sont de couleur rouge.
Le joueur mise sur un num�ro compris entre 0 et 49. En choisissant son num�ro, il y d�pose la somme qu'il souhaite miser.
Le croupier lance la roulette, l�che la bille et quand la roulette s'arr�te, rel�ve le num�ro de la case dans laquelle la bille s'est arr�t�e. Le num�ro sur lequel s'est arr�t�e la bille est, naturellement, le num�ro gagnant.
Si le num�ro gagnant est celui sur lequel le joueur a mis�, le croupier lui remet 3 fois la somme mis�e.
Sinon, le croupier regarde si le num�ro mis� par le joueur est de la m�me couleur que le num�ro gagnant. Si c'est le cas, le croupier lui remet 50 % de la somme mis�e. Si ce n'est pas le cas, le joueur perd sa mise.""")
print ''

while True:
    Argent_ch = raw_input("Argent initial en $:")
    try:
        Argent=int(Argent_ch)
    except:
        continue
    if Argent > 0 :
        break
Arginit = Argent
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
         print 'Vous avez perdu la moiti� de votre mise ' + str(m) + '$'
         Argent = Argent - m
         print '*****Money : {}$*****'.format(Argent)
    else :
        print 'Desole vous avez perdu {}$'.format(m)
        Argent = Argent - m
        print '*****Money : {}$*****'.format(Argent)
    
    
    if Argent == 0 : 
        break
    test = again()
    if test :
        continue
    else:
        break
print 'Thank you for playing ZCasino'
if Argent > Arginit :
    w = Argent - Arginit
    print 'Vous avez gagnez en tatal {}$'.format(w)
elif Argent < Arginit :
    w = Arginit - Argent
    print 'Vous avez perdu en tatal {}$'.format(w)
else:
    print "Tu n'as rien perdu n'i gagner "
    
os.system("pause") 
