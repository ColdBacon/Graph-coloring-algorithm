# !/usr/bin/python3
import numpy as np
import random
import module_graph as grafy

txt = []  # dane wejściowe z pliku
tablica = []  # zmiana na int wyjsciowego pliku
macierz = []
slownik = {}  # wierzcholek:kolor
n = 0  # ilosc wierzcholkow
lista_posortowanych = []
plik_z_krawedziami = 'krawedzie.txt'
szansa_mutacji = 0.2
MAX = 20  # limit of the iterations
populacja_poczatkowa = 10  # ilosc osobnikow w populacji losowej
NC = 0  # najlepsza wartosc jaka chcemy osiagnac
NB = 0  # ilosc wykonanych iteracji
wspolczynnik_odrzucenia = 0.2

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

#lista do kolorowanie zwyklego zachlannego
lista_1_do_n = [i for i in range(1, n + 1)]

#macierz
macierz = [[0 for i in range(n)] for j in range(n)]
for [x,y] in tablica:
    macierz[x-1][y-1] = 1
    macierz[y-1][x-1] = 1

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
graf2 = grafy.Graf(macierz = macierz, lista_wierzcholkow=lista_1_do_n)
graf1 = grafy.Graf(macierz = macierz, lista_wierzcholkow=lista_posortowanych)
print("Ilosc kolorow: ", grafy.Graf.ilosc_kolorow(graf2),"\nGRAF ZACHLANNY:",graf2.slownik_kolorow,"\nSUMA KWADRATOW KOLOROW:",grafy.Graf.fitting(graf2))
print("Ilosc kolorow dla listy posortowanej: ", grafy.Graf.ilosc_kolorow(graf1),"\nGRAF POSORTOWANY: ",graf1.slownik_kolorow)

#cialo algorytmu genetycznego
#populacja poczatkowa- kolorowanie na podstawie listy kolejnych wierzcholkow zaczynajacych sie od kolejnych nieparzystych wierzcholkow
for i in range(populacja_poczatkowa):
    lista_z_wierzcholkami = [i for i in range(1,n+1)]
    for j in range(1,2*i+1):
        lista_z_wierzcholkami.remove(j)
        lista_z_wierzcholkami.append(j)
    graf = grafy.Graf(macierz = macierz, lista_wierzcholkow=lista_z_wierzcholkami)  # inicjalizacja nowego grafu

grafy.Graf.odrzucanie_populacji(0.2)  # sortowanie populacji jest zapewnione poprzez wywolanie funkcji sortowanie_populacji wewnatrz odrzucanie_populacji

#zmienic na sume kwadratow kolorow
NC = grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0]) - 2
for i in grafy.Graf.lista_grafow:
    print("ILOSC KOLOROW: ",grafy.Graf.ilosc_kolorow(i))

while (NB < MAX and NC < grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0])):  # petla konczy sie po wykonaniu MAX ieracji lub po osiagnieciu celu
    #M = [[random.randint(1,100) for i in range((len(grafy.Graf.lista_grafow)))] for j in range(len(grafy.Graf.lista_grafow))]
    najlepszy_graf = grafy.Graf.lista_grafow[0]
    najlepszy_graf2 = grafy.Graf.lista_grafow[1]

    if najlepszy_graf != najlepszy_graf2:
        nowy_graf = grafy.Graf.krzyzowanie(najlepszy_graf, najlepszy_graf2)
        if (random.randint(1, 100) <= szansa_mutacji * 100):
            print ("MUTOWANIE!")
            nowy_graf.mutacja()
        nowy_graf.szukanie_bledow()
        nowy_graf2 = grafy.Graf.krzyzowanie(najlepszy_graf2, najlepszy_graf)
        if (random.randint(1, 100) <= szansa_mutacji * 100):
            print ("MUTOWANIE!")
            nowy_graf2.mutacja()
        nowy_graf2.szukanie_bledow()

    grafy.Graf.odrzucanie_ilosci(20)
    for i in range(len(grafy.Graf.lista_grafow)):
        print("graf nr:",i,"ilosc kolorow:",grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[i]),grafy.Graf.lista_grafow[i].slownik_kolorow)
    print("dlugosc listy: ",len(grafy.Graf.lista_grafow))
    print("ilosc kolorow: ",grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[0]))
    print("\nNAJLEPSZE GRAFY:")
    for i in range (5):
        print("Graf nr: ",i,grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[i]),grafy.Graf.lista_grafow[i].slownik_kolorow)
    NB += 1
    print("NB: ",NB,"\nKOLEJNA ITERACJA\n\n")
    print (100*'-')

for i in range(len(grafy.Graf.lista_grafow)):
    grafy.Graf.lista_grafow[i].error_correcting()

grafy.Graf.sortowanie_koncowe()

for i in range(5):
    print("graf nr:",i,"ilosc kolorow:",grafy.Graf.ilosc_kolorow(grafy.Graf.lista_grafow[i]),grafy.Graf.lista_grafow[i].slownik_kolorow)
    grafy.Graf.lista_grafow[i].check()
    print("-----")


