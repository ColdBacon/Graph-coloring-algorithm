#!/usr/bin/python3
import random
from itertools import permutations
txt=[]      #dane wejściowe z pliku
tablica=[]  #zmiana na int wyjsciowego pliku
slownik={}  #wierzcholek:kolor
slownik_2={}
n=0         #ilosc wierzcholkow
lista_posortowanych=[]
plik_z_krawedziami='graff0.3.txt'

def max_slownik(slowniki):      #zwraca ilosc kolorow
    maxi=0
    for x in slowniki.values():
        if x>maxi:
            maxi=x
    return maxi

def kolorowanie(macierz_polaczen,lista_krawedzi):       #funkcja kolorujaca zachlannie i zwracajaca slownik {indeks_wierzcholka:numer_koloru}
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

def losowanie_liczb(n):                         #zwraca liste z losowa kolejnoscia wierzcholkow
    lista_losowa=[i for i in range(1,n+1)]
    permutacja=list(permutations(lista_losowa))
    a=random.randint(0,len(permutacja))
    return permutacja[a]

def lista_kolorow(slownik_kolorow):             #zwraca tablice kolorow
    a=[i for i in slownik_kolorow.values()]
    return a

with open(plik_z_krawedziami) as plik:
    for linia in plik:
        if(len(linia.strip().split())>1):
            txt.append(linia.strip().split())
        else:
            for x in linia.strip().split():
                n=int(x)

for i in range(n):
    slownik[i+1]=-1
    slownik_2[i+1]=-1

for [x,y] in txt:
    y=int(y)
    x=int(x)
    tablica.append([x,y])

lista_1_do_n=[i for i in range(1,n+1)]
slownik = kolorowanie(tablica,lista_1_do_n)
print("Ilość kolorow:",max_slownik(slownik))

#zachlanny ulepszony
print(40*"-")
stopnie_wierzcholkow = {}
for x in range(1,n+1):
    stopnie_wierzcholkow[x]=0

for [x,y] in tablica:
    stopnie_wierzcholkow[x]+=1
    stopnie_wierzcholkow[y]+=1

posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1], reverse=True) #wierzcholki posortowane po stopniu

for x in posortowane_wierzcholki:
    lista_posortowanych.append(x[0])
slownik_2=kolorowanie(tablica,lista_posortowanych)

liczba_kolorow = max_slownik(slownik_2)
print("Ilosc kolorow: ",liczba_kolorow)






M = [[0 for i in range(n)] for j in range(n)] #tabu matrix
slownik_LF=kolorowanie(tablica,lista_posortowanych)

print(lista_kolorow(slownik_2))

NB = 0
s = slownik_2 #initial confugiration generated with a greedy algorithm
NC = liczba_kolorow - 1
MAX  = 10 #limit of the iterations

#deklarowanie zmiennnych globalnych na górze!!!

#while (NB<MAX):
    #s_best = s

    #while (f_best > 0 and NB < MAX):
        