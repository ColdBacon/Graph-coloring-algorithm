
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
szansa_mutacji = 0.02
szansa_krzyzowanie = 0.5
MAX  = 10 #limit of the iterations
populacja_poczatkowa = 10 #ilosc osobnikow w populacji losowej
NC = 0      #najlepsza wartosc jaka chcemy osiagnac

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
print("Ilosc kolorow: ",grafy.Graf.max_slownik(graf2))
'''print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.sortowanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.odrzucanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)'''
grafy.Graf.krzyzowanie(graf1,graf2)
grafy.Graf.sortowanie_populacji()
for x in grafy.Graf.lista_grafow:
    print(x.slownik_kolorow)
    print(40*"-")

print("cokolwiek ",grafy.Graf.lista_grafow[0].slownik_kolorow)

M = [[0 for i in range(n)] for j in range(n)] #tabu matrix

NB = 0
s = graf1.slownik_kolorow #initial confugiration generated with a greedy algorithm
MAX  = 10 #limit of the iterations

#deklarowanie zmiennnych globalnych na górze!!!

#cialo algorytmu genetycznego
for i in range(populacja_poczatkowa):
    lista_z_wierzcholkami = losowanie_listy_wierzcholkow(n)                         #losowanie kolejnosci w ktorej maja byc pokolorowane wierzcholki
    graf = grafy.Graf(macierz = tablica, lista_wierzcholkow = lista_z_wierzcholkami)#inicjalizacja nowego grafu
grafy.Graf.odrzucanie_populacji(0.2)        #sortowanie populacji jest zapewnione poprzez wywolanie funkcji sortowanie_populacji wewnatrz odrzucanie_populacji

NC = grafy.Graf.max_slownik(grafy.Graf.lista_grafow[0]) - 1  

while(NB<MAX or NC>=grafy.Graf.max_slownik(grafy.Graf.lista_grafow[0])):        #petla konczy sie po wykonaniu MAX ieracji lub po osiagnieciu celu
    lista_1_do_ilosc_grafow = [i for i in range(len(grafy.Graf.lista_grafow))]
    
    NB+=1

#while (NB<MAX):
    #s_best = s

    #while (f_best > 0 and NB < MAX):
