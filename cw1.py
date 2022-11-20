# -*- coding: utf-8 -*-


def konwertToHex(a):
    print(hex(a))

def konwertToBin(a):
    print(bin(a))

def podzielnosc2(a):
    if(a%2 == 0): print("Podzielna")
    else: print("Niepodzielna")

def podzielnosc7(a):
    if(a%7 == 0): print("Podzielna")
    else: print("Niepodzielna")

def kalkulator():
        print("Wybierz opcje: \n1. Konwertuj na hex\n2. Konwertuj na bin\n3."+
              " Podzielnosc przez 2\n4. Podzielnosc przez 7")
        wybor = int(input())
        print("Podaj liczbe:")
        liczba = int(input())
        if(wybor == 1): konwertToHex(liczba)
        elif(wybor == 2): konwertToBin(liczba)
        elif(wybor == 3): podzielnosc2(liczba)
        elif(wybor == 4):podzielnosc7(liczba)
    
kalkulator()        #wywołanie

##########

def BMI():
    print("Podaj wzrost (w metrach):")
    a = float(input())
    print("Podaj wage:")
    b = float(input())
    bmi = b/(a**2) 
    print("BMI wynosi: ", round(bmi,1))
    if(bmi<18.5): print("Niedowaga")
    elif(bmi>=18.5 and bmi<24.9): print("Prawidlowa waga")
    elif(bmi>=25.0 and bmi<30): print("Nadwaga")
    elif(bmi>=30): print("Otylosc")
    
BMI()               #wywołanie


