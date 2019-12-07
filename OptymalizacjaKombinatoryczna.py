
#!/usr/bin/python3
import random
from itertools import permutations
import module_graph as grafy

txt=[]      #dane wejściowe z pliku
tablica=[]  #zmiana na int wyjsciowego pliku
slownik={}  #wierzcholek:kolor
n=0         #ilosc wierzcholkow
lista_posortowanych=[]
plik_z_krawedziami='graff0.3.txt'
szansa_mutacji = 0.01

def losowanie_listy_wierzcholkow(n):                         #zwraca liste z losowa kolejnoscia wierzcholkow
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

for [x,y] in txt:
    y=int(y)
    x=int(x)
    tablica.append([x,y])

lista_1_do_n=[i for i in range(1,n+1)]

#zachlanny ulepszony
stopnie_wierzcholkow = {}
for x in range(1,n+1):
    stopnie_wierzcholkow[x]=0

for [x,y] in tablica:
    stopnie_wierzcholkow[x]+=1
    stopnie_wierzcholkow[y]+=1

posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1], reverse=True) #wierzcholki posortowane po stopniu

for x in posortowane_wierzcholki:
    lista_posortowanych.append(x[0])

#zachlanny ulepszony, użycie Graf.py
print(40*"-")
graf2 = grafy.Graf(macierz = tablica,lista_wierzcholkow = lista_1_do_n)
graf1 = grafy.Graf(macierz = tablica,lista_wierzcholkow = lista_posortowanych)
print("Ilosc kolorow: ",grafy.max_slownik(graf2.slownik_kolorow))
'''print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.sortowanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.odrzucanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)'''
grafy.Graf.krzyzowanie(graf1,graf2)
for x in grafy.Graf.lista_grafow:
    print(x)
    print(40*"-")

M = [[0 for i in range(n)] for j in range(n)] #tabu matrix

NB = 0
s = graf1.slownik_kolorow #initial confugiration generated with a greedy algorithm
NC = grafy.max_slownik(grafy.Graf.lista_grafow[0]) - 1      #wczesniej trzeba posortowac lista_grafow
MAX  = 10 #limit of the iterations

#deklarowanie zmiennnych globalnych na górze!!!

#while (NB<MAX):
    #s_best = s

    #while (f_best > 0 and NB < MAX):
