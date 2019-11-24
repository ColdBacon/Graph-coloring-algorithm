#!/usr/bin/python3
import random
from itertools import permutations
txt=[]      #dane wejściowe z pliku
tablica=[]  #zmiana na int wyjsciowego pliku
slownik={}  #wierzcholek:kolor
slownik_2={}
n=0         #ilosc wierzcholkow
lista_posortowanych=[]

def max_slownik(slowniki):
    maxi=0
    for x in slowniki.values():
        if x>maxi:
            maxi=x
    return maxi

def kolorowanie(macierz_polaczen,lista_krawedzi):
    lista_wychodzacych=[]   #lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
    slownik_kolorow={}
    for i in range(1,len(lista_krawedzi)+1):
        slownik_kolorow[i]=0
    kolor=0                 #numery oznaczają kolory
    for i in lista_krawedzi:
        for [x,y] in macierz_polaczen:
            if x==i:
                lista_wychodzacych.append(y)
            elif y==i:
                lista_wychodzacych.append(x)
        for li in lista_wychodzacych:
            if slownik_kolorow[li]==kolor:
                kolor+=1
        slownik_kolorow[i]=kolor
        lista_wychodzacych=[]
        kolor=1
    return slownik_kolorow

def losowanie_liczb(n):
    lista_losowa=[i for i in range(n)]
    permutacja=list(permutations(lista_losowa))
    a=random.randint(0,len(permutacja))
    return permutacja[a]

with open('graff0.3.txt') as plik:
    for linia in plik:
        if(len(linia.strip().split())>1):
            txt.append(linia.strip().split())
        else:
            for x in linia.strip().split():
                n=int(x)
print(n)
for i in range(n):
    slownik[i+1]=-1
    slownik_2[i+1]=-1

for [x,y] in txt:
    y=int(y)
    x=int(x)
    tablica.append([x,y])

kolor=1             #numery oznaczają kolory
lista_wychodz=[]    #lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
for i in range(1,n+1):
    for [x,y] in tablica:
        if x==i:
            lista_wychodz.append(y)
        elif y==i:
            lista_wychodz.append(x)
    for li in lista_wychodz:
        if slownik[li]==kolor:
            kolor+=1
    slownik[i]=kolor
    lista_wychodz=[]
    kolor=1

print("Ilość kolorow:",max_slownik(slownik))

print(40*"-")
stopnie_wierzcholkow = {}
for x in range(1,n+1):
    stopnie_wierzcholkow[x]=0

for [x,y] in tablica:
    stopnie_wierzcholkow[x]+=1
    stopnie_wierzcholkow[y]+=1

posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1], reverse=True)

for x in posortowane_wierzcholki:
    lista_posortowanych.append(x[0])

for i in lista_posortowanych:
    for [x,y] in tablica:
        if x==i:
            lista_wychodz.append(y)
        elif y==i:
            lista_wychodz.append(x)
    for li in lista_wychodz:
        if slownik_2[li]==kolor:
            kolor+=1
    slownik_2[i]=kolor
    lista_wychodz=[]
    kolor=1

liczba_kolorow = max_slownik(slownik_2)
print("Ilosc kolorow: ",liczba_kolorow)

M = [[0 for i in range(n)] for j in range(n)] #tabu matrix
slownik_LF=kolorowanie(tablica,lista_posortowanych)
print(max_slownik(slownik_LF))

NB = 0
s = slownik_2 #initial confugiration generated with a greedy algorithm
NC = liczba_kolorow - 1
MAX  = 10 #limit of the iterations

#while (NB<MAX):
    #s_best = s

    #while (f_best > 0 and NB < MAX):
        