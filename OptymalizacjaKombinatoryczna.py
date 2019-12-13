# !/usr/bin/python3
import numpy as np
import random
import module_graph as grafy

txt = []  # dane wejściowe z pliku
tablica = []  # zmiana na int wyjsciowego pliku
slownik = {}  # wierzcholek:kolor
n = 0  # ilosc wierzcholkow
lista_posortowanych = []
plik_z_krawedziami = 'graph70.txt'
szansa_mutacji = 0.02
szansa_krzyzowanie = 0.25
MAX = 5  # limit of the iterations
populacja_poczatkowa = 10  # ilosc osobnikow w populacji losowej
NC = 0  # najlepsza wartosc jaka chcemy osiagnac
NB = 0  # ilosc wykonanych iteracji
wspolczynnik_odrzucenia = 0.2

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
print("wszystkie slowniki: ",grafy.Graf.lista_grafow)
nowy_graf = grafy.Graf.krzyzowanie(graf1, graf2)
grafy.Graf.sortowanie_populacji()
for x in grafy.Graf.lista_grafow:
    print("SLOWNIK KOLOROW: ",x.slownik_kolorow)
    print(40 * "-")
'''
s = graf1.slownik_kolorow  # initial confugiration generated with a greedy algorithm

# cialo algorytmu genetycznego
for i in range(populacja_poczatkowa):
    lista_z_wierzcholkami=losowanie_listy_wierzcholkow(n)  # losowanie kolejnosci w ktorej maja byc pokolorowane wierzcholki
    graf = grafy.Graf(macierz=tablica, lista_wierzcholkow=lista_z_wierzcholkami)  # inicjalizacja nowego grafu
grafy.Graf.odrzucanie_populacji(0.2)  # sortowanie populacji jest zapewnione poprzez wywolanie funkcji sortowanie_populacji wewnatrz odrzucanie_populacji

NC = grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0]) - 1
for i in grafy.Graf.lista_grafow:
    print("ILOSC KOLOROW: ",grafy.Graf.ilosc_kolorow(i))

while (NB < MAX or NC >= grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0])):  # petla konczy sie po wykonaniu MAX ieracji lub po osiagnieciu celu
    #lista_1_do_ilosc_grafow = [i for i in range(len(grafy.Graf.lista_grafow))]
    #M = [[random.randint(1,100) for i in range((len(grafy.Graf.lista_grafow)))] for j in range(len(grafy.Graf.lista_grafow))]
    wierzcholek = random.randint(1,n)
    wierzcholek2 = random.randint(1,n)
    wierzcholek3 = random.randint(1,n)
    wierzcholek4 = random.randint(1,n)
    lol = len(grafy.Graf.lista_grafow)
    print("wierz1",wierzcholek,"wierz2",wierzcholek2,"wierz3",wierzcholek3,"wierz4",wierzcholek4)
    najlepsza_suma = grafy.Graf.lista_grafow[0].slownik_kolorow[wierzcholek] + grafy.Graf.lista_grafow[0].slownik_kolorow[wierzcholek2]
    najlepsza_suma2 = grafy.Graf.lista_grafow[0].slownik_kolorow[wierzcholek3] + grafy.Graf.lista_grafow[0].slownik_kolorow[wierzcholek4]
    najlepszy_graf = grafy.Graf.lista_grafow[0]
    najlepszy_graf2 = grafy.Graf.lista_grafow[0]

    for i in range(1,lol):
        suma = grafy.Graf.lista_grafow[i].slownik_kolorow[wierzcholek] + grafy.Graf.lista_grafow[i].slownik_kolorow[wierzcholek2]
        suma2 = grafy.Graf.lista_grafow[i].slownik_kolorow[wierzcholek3] + grafy.Graf.lista_grafow[i].slownik_kolorow[wierzcholek4]
        if suma<najlepsza_suma:
            najlepszy_graf = grafy.Graf.lista_grafow[i]
            najlepsza_suma = suma
        if suma2<najlepsza_suma2:
            najlepszy_graf2 = grafy.Graf.lista_grafow[i]
            najlepsza_suma2 = suma2

    if najlepszy_graf != najlepszy_graf2:
        nowy_graf = grafy.Graf.krzyzowanie(najlepszy_graf, najlepszy_graf2)
        if (random.randint(1, 100) <= szansa_mutacji * 100):
            nowy_graf.mutacja()
            nowy_graf.szukanie_bledow()
        nowy_graf = grafy.Graf.krzyzowanie(najlepszy_graf2, najlepszy_graf)
        if (random.randint(1, 100) <= szansa_mutacji * 100):
            nowy_graf.mutacja()
            nowy_graf.szukanie_bledow()

    """
    for i in range(n):
        for j in range(n):
            if (i != j and M[i][j]<=szansa_krzyzowanie*100):
                nowy_graf = grafy.Graf.krzyzowanie(grafy.Graf.lista_grafow[i], grafy.Graf.lista_grafow[j])
                if(random.randint(1,100)<=szansa_mutacji*100):
                    nowy_graf.mutacja()
                    nowy_graf.szukanie_bledow()
    """
    grafy.Graf.odrzucanie_ilosci(20)
    print("dlugosc listy: ",len(grafy.Graf.lista_grafow))
    print("ilosc kolorow: ",grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0]))
    for i in range (5):
        print("Graf nr: ",i,grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[i]),grafy.Graf.lista_grafow[i].slownik_kolorow)
    NB += 1
    print("NB: ",NB)

