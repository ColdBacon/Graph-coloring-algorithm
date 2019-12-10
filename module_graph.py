#!/usr/bin/python3
import random
import numpy as np
from itertools import permutations

class Graf:  # klasa graf przechowuje pokolorowane wierzcholki grafu

    lista_grafow = []  # lista przechowuje wszystkie pokolorowania (slowniki) w populacji (pole statyczne)

    def kolorowanie(self,lista_wierzcholkow):  # funkcja kolorujaca zachlannie i zwracajaca slownik {indeks_wierzcholka:numer_koloru}
        lista_wychodzacych = []  # lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
        slownik_kolorow = {}
        for i in range(1, len(lista_wierzcholkow) + 1):
            slownik_kolorow[i] = 0
        kolor = 0  # numery oznaczają kolory
        for i in lista_wierzcholkow:
            for [x, y] in self.macierz:
                if x == i:
                    lista_wychodzacych.append(y)
                elif y == i:
                    lista_wychodzacych.append(x)
            for li in lista_wychodzacych:
                if slownik_kolorow[li] == kolor:
                    kolor += 1
            slownik_kolorow[i] = kolor
            lista_wychodzacych = []
            kolor = 1
        return slownik_kolorow

    def __init__(self, macierz, lista_wierzcholkow=None, slownik_kolorow=None):  # inicjalizacja grafu
        if (slownik_kolorow == None):
            self.macierz = macierz
            self.lista_bledow = []
            self.slownik_kolorow = self.kolorowanie(lista_wierzcholkow)  # kolorowanie grafu, slownik {wierzcholek:kolor}
            Graf.lista_grafow.append(self)  # dodawanie slownikow do listy
        elif (lista_wierzcholkow == None):
            self.macierz = macierz
            self.slownik_kolorow = slownik_kolorow
            self.lista_bledow = self.szukanie_bledow
            Graf.lista_grafow.append(self)

    def szukanie_bledow(self):
        lista_blednych = []
        for [x, y] in self.macierz:
            if (x not in lista_blednych or y not in lista_blednych):
                continue
            if (self.slownik_kolorow[x] == self.slownik_kolorow[y]):
                lista_blednych.append(y)
        return lista_blednych

    def kolorowanie_jednego(self, wierzcholek):
        lista_kolor = []
        for [x, y] in self.macierz:
            if (wierzcholek == x):
                lista_kolor.append(self.slownik_kolorow[y])
            elif (wierzcholek == y):
                lista_kolor.append(self.slownik_kolorow[x])
        lista_kolor.sort()
        for i in range(1,len(lista_kolor)+1):
            if (i not in lista_kolor):
                self.slownik_kolorow[wierzcholek]=i

    @staticmethod
    def ilosc_kolorow(graf1):  # zwraca ilosc kolorow danego grafu
        maxi = 0
        for x in graf1.slownik_kolorow.values():
            if x > maxi:
                maxi = x
        return maxi

    @staticmethod
    def sortowanie_populacji():
        Graf.lista_grafow.sort(key=Graf.ilosc_kolorow)

    @staticmethod
    def odrzucanie_populacji(wspolczynnik):  # odrzucamy wspolczynnik*100% najgorszych grafow (z najwieksza iloscia kolorow)
        Graf.sortowanie_populacji()
        Graf.lista_grafow = Graf.lista_grafow[0:round(len(Graf.lista_grafow) * (1 - wspolczynnik))]

    @staticmethod
    def krzyzowanie(graf1, graf2):  # metoda krzyzujaca dwa grafy
        slownik = {}
        for x in range(1, len(graf1.slownik_kolorow) + 1):
            if (x < (len((graf1.slownik_kolorow)) // 2) + 1):
                slownik[x] = graf1.slownik_kolorow[x]
            else:
                slownik[x] = graf2.slownik_kolorow[x]
        nowy_graf = Graf(macierz=graf1.macierz, slownik_kolorow=slownik)
        return nowy_graf

    def mutacja(self):
        lista_z_kolorami = []  # lista przechowuje kolory ktore musi permutowac
        for kolor in self.slownik_kolorow.values():
            lista_z_kolorami.append(kolor)
        """"
        permutacje = list(permutations(lista_z_kolorami))
        a = random.randint(0, len(permutacje))
        lista_z_kolorami = permutacje[a]
        """
        permutacja = list(np.random.permutation(lista_z_kolorami))
        lista_z_kolorami = permutacja
        for x in range(len(lista_z_kolorami)):
            self.slownik_kolorow[x + 1] = lista_z_kolorami[x]