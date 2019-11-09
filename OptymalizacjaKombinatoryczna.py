#!/usr/bin/python3
txt=[]      #dane wejściowe z pliku
tablica=[]  #zmiana na int wyjsciowego pliku
slownik={}  #wierzcholek:kolor
slownik_2={}
n=0         #ilosc wierzcholkow
lista_posortowanych=[]


with open('krawedzie.txt') as plik:
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
    print(i,lista_wychodz)
    for li in lista_wychodz:
        if slownik[li]==kolor:
            kolor+=1
    slownik[i]=kolor
    lista_wychodz=[]
    kolor=1

maxi=0
for x in slownik.values():
    if x>maxi:
        maxi=x

print("Ilość kolorow:",maxi)


print(40*"-")
TABLICA = []
for [x,y] in txt:
    y=int(y)
    x=int(x)
    TABLICA.append([x,y])
print("Tablica:",TABLICA)

stopnie_wierzcholkow = {}
for x in range(1,n+1):
    stopnie_wierzcholkow[x]=0

for [x,y] in tablica:
    stopnie_wierzcholkow[x]+=1
    stopnie_wierzcholkow[y]+=1

print ("stopnie:",stopnie_wierzcholkow)

posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1], reverse=True)
print("posortowane:",posortowane_wierzcholki)

for x in posortowane_wierzcholki:
    lista_posortowanych.append(x[0])

print(lista_posortowanych)

for i in lista_posortowanych:
    for [x,y] in tablica:
        if x==i:
            lista_wychodz.append(y)
        elif y==i:
            lista_wychodz.append(x)
    print(i,lista_wychodz)
    for li in lista_wychodz:
        if slownik[li]==kolor:
            kolor+=1
    slownik_2[i]=kolor
    lista_wychodz=[]
    kolor=1

print(slownik_2)