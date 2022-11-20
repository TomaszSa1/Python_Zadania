# -*- coding: utf-8 -*-


#parzystosc


def parzystosc(a):
    if a%2 == 0: 
        print("Parzysta") 
        return 1
    else: 
        print("Nieparzysta")
        return 0
    
parzystosc(int(input("Podaj liczbe:\n"))) #wywołanie

####################################

#liczby z przedziału

for i in range(-7,14):
    print(i)
    
i = -7    
while i < 14:
    print(i)
    i+=1
    


def wypisz():    #funkcja wupisująca z danego zakresu
    a = int(input("Podaj początek przedzialu:\n"))
    b = int(input("Podaj koniec przedzialu:\n"))
    for i in range(a,b+1):
        print(i)

wypisz()        #wywołanie


def parzystoscWypisz(a):        #funkcja parzystosc ale bez printow
    if a%2 == 0: 
        return 1
    else: 
        return 0
    


def wypiszParzyste():    #funkcja wypisująca parzyste liczby przedziału
    a = int(input("Podaj początek przedzialu:\n"))
    b = int(input("Podaj koniec przedzialu:\n"))
    for i in range(a,b+1):
        if parzystoscWypisz(i): 
            print(i)

wypiszParzyste()    #wywołanie
    
####################################

#lista

lista = []
for r in range (3,7):
    lista.append(r)
print (lista)

n=0                   #wyznacznik pozycji
while(n<len(lista)): 
    print(lista[n]) 
    n+=1
    

a = 'ala'
b = 'kot'

def pierwsza_litera(s):
    print("Pierwsza litera to: ",s[0])
    return s[0]
pierwsza_litera(a)      #wywołanie

def przeliteruj(s):
    for i in s:
        print (i)

przeliteruj(a)          #wywołanie

c = 'ala kot'

lista = []
for i in c:
    lista.append(i)

print(lista)

print(list(c)) 

def ostatnia_litera(s):
    print("Ostatnia litera to: ", s[len(s)-1])    
    
ostatnia_litera(c)      #wywołanie


print(c.replace("kot","pies"))

c = 'ala kot'


print('Pierwsze slowo to: ', c.split()[0].upper())


print(c.replace('a', ''))

#########################################

#wykrzykniki

def wykrzykniki(s):
    c = s
    for i in range(0,s.count('!')*2):
        c+='!'
    print(c)
        
wykrzykniki("czesc!!") #wywołanie


############################################

#Login

def pierwsza_litera_l(s):
    return s[0]




def Login():
    s = input("Podaj imie i nazwisko: \n")
    k = s.split()
    login = pierwsza_litera_l(k[0]) + pierwsza_litera_l(k[1])
    login += str(len(k[0])) + str(len(k[1]))
    print(login)
    return login

Login()     #wywołanie


############################################

#Katy

import math

def katy():
    k = float(input("Podaj kat: \n"))
    rad_k = math.radians(k)
    print(k, rad_k, math.sin(rad_k), math.cos(rad_k))
    
katy()          #wywołanie



