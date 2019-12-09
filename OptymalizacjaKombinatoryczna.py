# !/usr/bin/python3
import numpy as np
import random
import module_graph as grafy

txt = []  # dane wejściowe z pliku
tablica = []  # zmiana na int wyjsciowego pliku
slownik = {}  # wierzcholek:kolor
n = 0  # ilosc wierzcholkow
lista_posortowanych = []
plik_z_krawedziami = 'graff0.3.txt'
szansa_mutacji = 0.02
szansa_krzyzowanie = 0.5
MAX = 10  # limit of the iterations
populacja_poczatkowa = 10  # ilosc osobnikow w populacji losowej
NC = 0  # najlepsza wartosc jaka chcemy osiagnac
NB = 0  # ilosc wykonanych iteracji

def losowanie_listy_wierzcholkow(n):  # zwraca liste z losowa kolejnoscia wierzcholkow
    lista_losowa = [i for i in range(1, n + 1)]
    permutacja = list(np.random.permutation(lista_losowa))
    return permutacja

def lista_kolorow(slownik_kolorow):  # zwraca tablice kolorow
    a = [i for i in slownik_kolorow.values()]
    return a

with open(plik_z_krawedziami) as plik:
    for linia in plik:
        if (len(linia.strip().split()) > 1):
            txt.append(linia.strip().split())
        else:
            for x in linia.strip().split():
                n = int(x)

for [x, y] in txt:
    y = int(y)
    x = int(x)
    tablica.append([x, y])

lista_1_do_n = [i for i in range(1, n + 1)]

# zachlanny ulepszony
stopnie_wierzcholkow = {}
for x in range(1, n + 1):
    stopnie_wierzcholkow[x] = 0

for [x, y] in tablica:
    stopnie_wierzcholkow[x] += 1
    stopnie_wierzcholkow[y] += 1

# wierzcholki posortowane po stopniu
posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1],reverse=True)

for x in posortowane_wierzcholki:
    lista_posortowanych.append(x[0])

# zachlanny ulepszony, użycie Graf.py
graf2 = grafy.Graf(macierz=tablica, lista_wierzcholkow=lista_1_do_n)
graf1 = grafy.Graf(macierz=tablica, lista_wierzcholkow=lista_posortowanych)
print("Ilosc kolorow: ", grafy.Graf.ilosc_kolorow(graf2))
print("Ilosc kolorow dla listy posortowanej: ", grafy.Graf.ilosc_kolorow(graf1))

'''print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.sortowanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
grafy.Graf.odrzucanie_populacji()
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)'''
grafy.Graf.krzyzowanie(graf1, graf2)
grafy.Graf.sortowanie_populacji()
for x in grafy.Graf.lista_grafow:
    print("SLOWNIK KOLOROW: ",x.slownik_kolorow)
    print(40 * "-")

M = [[0 for i in range(n)] for j in range(n)]  # tabu matrix

s = graf1.slownik_kolorow  # initial confugiration generated with a greedy algorithm

# cialo algorytmu genetycznego
for i in range(populacja_poczatkowa):
    lista_z_wierzcholkami=losowanie_listy_wierzcholkow(n)  # losowanie kolejnosci w ktorej maja byc pokolorowane wierzcholki
    graf = grafy.Graf(macierz=tablica, lista_wierzcholkow=lista_z_wierzcholkami)  # inicjalizacja nowego grafu
grafy.Graf.odrzucanie_populacji(0.2)  # sortowanie populacji jest zapewnione poprzez wywolanie funkcji sortowanie_populacji wewnatrz odrzucanie_populacji

NC = grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0]) - 1

while (NB < MAX or NC >= grafy.Graf.ilosc_kolorow(
        grafy.Graf.lista_grafow[0])):  # petla konczy sie po wykonaniu MAX ieracji lub po osiagnieciu celu
    lista_1_do_ilosc_grafow = [i for i in range(len(grafy.Graf.lista_grafow))]
    NB += 1

# while (NB<MAX):
# s_best = s

# while (f_best > 0 and NB < MAX):