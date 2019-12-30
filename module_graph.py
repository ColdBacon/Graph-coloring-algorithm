#!/usr/bin/python3
import random
import numpy as np
from itertools import permutations

class Graf:  # klasa graf przechowuje pokolorowane wierzcholki grafu

    lista_grafow = []  # lista przechowuje wszystkie pokolorowania (slowniki) w populacji (pole statyczne)

    def kolorowanie_tablica(self,lista_wierzcholkow):  # funkcja kolorujaca zachlannie i zwracajaca slownik {indeks_wierzcholka:numer_koloru}
        lista_kolorow_sasiadow = []  # lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
        slownik_kolorow = {}
        for i in range(1, len(lista_wierzcholkow) + 1):
            slownik_kolorow[i] = 0
        for i in lista_wierzcholkow:
            for [x, y] in self.lista_krawedzi:
                if x == i:
                    lista_kolorow_sasiadow.append(slownik_kolorow[y])
                elif y == i:
                    lista_kolorow_sasiadow.append(slownik_kolorow[x])
            lista_kolorow_sasiadow.sort()
            for k in range(1, lista_kolorow_sasiadow[-1] + 2):
                if k not in lista_kolorow_sasiadow:
                    slownik_kolorow[i] = k
                    break
            lista_kolorow_sasiadow = []
        for [x,y] in self.lista_krawedzi:
            if slownik_kolorow [x] == slownik_kolorow[y]:
                print("WIERZCHOLKI SASIEDNIE MAJA TAKIE SAME KOLORY!")
        return slownik_kolorow

    def kolorowanie_macierz(self,lista_wierzcholkow):
        lista_kolorow_sasiadow = []  # lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
        slownik_kolorow = {}
        for i in range(1, len(lista_wierzcholkow) + 1):
            slownik_kolorow[i] = 0
        for i in lista_wierzcholkow:
            for j in range(len(self.macierz[i-1])):
                if self.macierz[i-1][j]:
                    lista_kolorow_sasiadow.append(slownik_kolorow[j+1])
            #print("lista kolorow: ",lista_kolorow_sasiadow)
            lista_kolorow_sasiadow.sort()
            for k in range(1, lista_kolorow_sasiadow[-1] + 2):
                if k not in lista_kolorow_sasiadow:
                    slownik_kolorow[i] = k
                    break
            lista_kolorow_sasiadow = []

        return slownik_kolorow

    def __init__(self, macierz, lista_wierzcholkow=None, slownik_kolorow=None):  # inicjalizacja grafu
        if (slownik_kolorow == None):
            self.macierz = macierz
            self.lista_bledow = []
            self.slownik_kolorow = self.kolorowanie_macierz(lista_wierzcholkow)  # kolorowanie grafu, slownik {wierzcholek:kolor}
            Graf.lista_grafow.append(self)  # dodawanie slownikow do listy
        elif (lista_wierzcholkow == None):
            self.macierz = macierz
            self.slownik_kolorow = slownik_kolorow
            self.lista_bledow = []
            self.lista_bledow = self.szukanie_bledow()
            Graf.lista_grafow.append(self)

    def kolorowanie_jednego(self, wierzcholek):
        print("zmiana koloru dla wierzcholka:",wierzcholek)
        lista_kolor = []
        for j in range(len(self.macierz[wierzcholek-1])):
            if self.macierz[wierzcholek-1][j]:
                lista_kolor.append(self.slownik_kolorow[j + 1])
        lista_kolor.sort()
        print ("lista kolorow: ",lista_kolor)
        for i in range(1,lista_kolor[-1]+2):
            if (i not in lista_kolor):
                print("stary: ",self.slownik_kolorow[wierzcholek],"nowy:",i)
                self.slownik_kolorow[wierzcholek]=i
                break

    def szukanie_bledow(self):
        lista_bledow = []
        for x in range(len(self.macierz)):
            for y in range(len(self.macierz)):
                if self.macierz[x][y]:
                    if (x+1 in lista_bledow or y+1 in lista_bledow):
                        continue
                    if (self.slownik_kolorow[x+1] == self.slownik_kolorow[y+1]):
                        lista_bledow.append(y+1)
        lista_bledow.sort()
        return lista_bledow

    def error_correcting(self):
        for error in self.lista_bledow:
            self.kolorowanie_jednego(error)

    @staticmethod
    def ilosc_kolorow(graf1):  # zwraca ilosc kolorow danego grafu
        maxi = 0
        for x in graf1.slownik_kolorow.values():
            if x > maxi:
                maxi = x
        return maxi

    @staticmethod
    def fitting(graf): #liczy sume kwadratow kolorow danego grafu
        suma = 0
        for kolor in graf.slownik_kolorow.values():
            suma = suma + kolor**2
            #print ("kolor:",kolor,"suma:",suma,"\n")
        return suma

    @staticmethod
    def sortowanie_populacji():
        Graf.lista_grafow.sort(key=Graf.fitting)

    @staticmethod
    def sortowanie_koncowe():
        Graf.lista_grafow.sort(key=Graf.ilosc_kolorow)

    @staticmethod
    def odrzucanie_populacji(wspolczynnik):  # odrzucamy wspolczynnik*100% najgorszych grafow (z najwieksza iloscia kolorow)
        Graf.sortowanie_populacji()
        Graf.lista_grafow = Graf.lista_grafow[0:round(len(Graf.lista_grafow) * (1 - wspolczynnik))]

    @staticmethod
    def odrzucanie_ilosci(wspolczynnik):
        Graf.sortowanie_populacji()
        Graf.lista_grafow = Graf.lista_grafow[0:min(wspolczynnik,len(Graf.lista_grafow))]

    @staticmethod
    def krzyzowanie(graf1, graf2):  # metoda krzyzujaca dwa grafy
        slownik = {}
        dzielnik = random.randint(1,9)
        for x in range(1, len(graf1.slownik_kolorow) + 1):
            if (x < (len((graf1.slownik_kolorow)) // dzielnik) + 1):
                slownik[x] = graf1.slownik_kolorow[x]
            else:
                slownik[x] = graf2.slownik_kolorow[x]
        nowy_graf = Graf(macierz = graf1.macierz, slownik_kolorow=slownik)
        return nowy_graf

    def mutacja(self):
        """
        lista_z_kolorami = []  # lista przechowuje kolory ktore musi permutowac
        for kolor in self.slownik_kolorow.values():
            lista_z_kolorami.append(kolor)
        permutacje = list(permutations(lista_z_kolorami))
        a = random.randint(0, len(permutacje))
        lista_z_kolorami = permutacje[a]
        permutacja = list(np.random.permutation(lista_z_kolorami))
        lista_z_kolorami = permutacja
        for x in range(len(lista_z_kolorami)):
            self.slownik_kolorow[x + 1] = lista_z_kolorami[x]
        """
        max_kolor = self.ilosc_kolorow(self)
        for wierzcholek,kolor in self.slownik_kolorow.items():
            if kolor == max_kolor or kolor == max_kolor-1:
                self.slownik_kolorow[wierzcholek] = 1

    def check(self):
        for x in range(len(self.macierz)):
            for y in range(len(self.macierz)):
                if self.macierz[x][y]:
                    if (self.slownik_kolorow[x + 1] == self.slownik_kolorow[y + 1]):
                        print("SASIEDZI MAJA TAKIE SAME KOLORY!",x+1,y+1)

            break