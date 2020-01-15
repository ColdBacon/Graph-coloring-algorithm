#!/usr/bin/python3
import random
from itertools import permutations

class Graf:  # klasa graf przechowuje pokolorowane wierzcholki grafu

    lista_grafow = []  # lista przechowuje wszystkie pokolorowania (slowniki) w populacji (pole statyczne)

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
            self.szukanie_bledow()
            Graf.lista_grafow.append(self)

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
            if len(lista_kolorow_sasiadow)>0:
                for k in range(1, lista_kolorow_sasiadow[-1] + 2):
                    if k not in lista_kolorow_sasiadow:
                        slownik_kolorow[i] = k
                        break
            else:
                slownik_kolorow[i]=1
            lista_kolorow_sasiadow = []

        return slownik_kolorow

    def kolorowanie_jednego(self, wierzcholek,value):
        #print("zmiana koloru dla wierzcholka:",wierzcholek)
        #print ("lista kolorow: ",lista_kolor)
        if value:
            lista_kolor = []
            if self.lista_bledow ==None:
                self.lista_bledow = []
            for j in range(len(self.macierz[wierzcholek-1])):
                if self.macierz[wierzcholek-1][j]:
                    if j+1 in self.lista_bledow:
                        #print ("wierzcholek",j+1,"jest w liscie bledow:",self.lista_bledow)
                        pass
                    else:
                        lista_kolor.append(self.slownik_kolorow[j + 1])

            lista_kolor.sort()
            for i in range(1,lista_kolor[-1]+2):
                if (i not in lista_kolor):
                    #print("stary: ",self.slownik_kolorow[wierzcholek],"nowy:",i)
                    self.slownik_kolorow[wierzcholek]=i
                    break
        else:
            lista_kolor = []
            if self.lista_bledow ==None:
                self.lista_bledow = []
            for j in range(len(self.macierz[wierzcholek-1])):
                if self.macierz[wierzcholek-1][j]:
                    lista_kolor.append(self.slownik_kolorow[j + 1])

            lista_kolor.sort()
            usuniete = False
            for i in range(1,self.slownik_kolorow[wierzcholek]):
                if (i not in lista_kolor):
                    #print("stary: ",self.slownik_kolorow[wierzcholek],"nowy:",i)
                    self.slownik_kolorow[wierzcholek]=i
                    usuniete = True
                    break
            return usuniete

    def szukanie_bledow(self):
        lista_bledow = []
        slownik_bledow = {}
        lista_posortowanych = []
        for x in range(len(self.macierz)):
            for y in range(len(self.macierz)):
                if self.macierz[x][y]:
                    if (x+1 in lista_bledow or y+1 in lista_bledow):
                        continue
                    if (self.slownik_kolorow[x+1] == self.slownik_kolorow[y+1]):
                        lista_bledow.append(y+1)

        index = 0

        for i in range(len(lista_bledow)):
            naprawa = self.kolorowanie_jednego(lista_bledow[index],False)
            # (lista_bledow[index],index,i)
            if naprawa:
                lista_bledow.remove(lista_bledow[index])
            else:
                index+=1

        for kolor in lista_bledow:
            ilosc_sasiadow = 0
            for i in range(len(self.macierz)):
                if self.macierz[kolor-1][i]:
                    ilosc_sasiadow+=1
            slownik_bledow[kolor]=ilosc_sasiadow

        posortowane_wierzcholki = sorted(slownik_bledow.items(), key=lambda x: x[1], reverse=True)
        for x in posortowane_wierzcholki:
            lista_posortowanych.append(x[0])

        #lista_bledow.sort()
        if lista_posortowanych == None:
            self.lista_bledow = []
        else:
            self.lista_bledow = lista_posortowanych

    def error_correcting(self):
            #self.lista_bledow = self.szukanie_bledow()
            #print("lista_bledow przed error_correcting", self.lista_bledow)
            for i in range(len(self.lista_bledow)):
                self.kolorowanie_jednego(self.lista_bledow[0],True)
                #print ("usuwam wierzcholek",self.lista_bledow[0]," z listy bledow",self.lista_bledow)
                self.lista_bledow.remove(self.lista_bledow[0])
            #print("lista_bledow po error_correcting", self.lista_bledow)

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
    def selection_operator(graf): #liczy jakosc grafow ze specjalnego wzoru
        suma = graf.ilosc_kolorow(graf) + len(graf.lista_bledow) * 2
        if len(graf.lista_bledow)>0:
            suma+=1
        return suma

    @staticmethod
    def sortowanie_populacji():
        Graf.lista_grafow.sort(key=Graf.fitting)
        #Graf.lista_grafow.sort(key=Graf.selection_operator)

    @staticmethod
    def sortowanie_koncowe():
        Graf.lista_grafow.sort(key=Graf.ilosc_kolorow)

    @staticmethod
    def odrzucanie_populacji(wspolczynnik):  # odrzucamy wspolczynnik*100% najgorszych grafow (z najwieksza iloscia kolorow)
        Graf.sortowanie_koncowe()
        Graf.lista_grafow = Graf.lista_grafow[0:round(len(Graf.lista_grafow) * (1 - wspolczynnik))]

    @staticmethod
    def odrzucanie_ilosci(wspolczynnik):
        Graf.sortowanie_koncowe()
        Graf.lista_grafow = Graf.lista_grafow[0:min(wspolczynnik,len(Graf.lista_grafow))]

    @staticmethod
    def krzyzowanie(graf1, graf2):  # metoda krzyzujaca dwa grafy
        slownik = {}
        dzielnik = random.randint(2,4)
        for x in range(1, len(graf1.slownik_kolorow) + 1):
            if (x < (len((graf1.slownik_kolorow)) // dzielnik) + 1): #or x>2*(len((graf1.slownik_kolorow)) // dzielnik)):
                slownik[x] = graf1.slownik_kolorow[x]
            else:
                slownik[x] = graf2.slownik_kolorow[x]
        exist = True
        for graf in Graf.lista_grafow:
            for x in range(1,len(graf1.macierz)+1):
                if slownik[x]==graf.slownik_kolorow[x]:
                    exist = False
                    break
            if exist == False:
                break
        if exist == True:
            print ("Taki sam slownik!")
        else:
            nowy_graf = Graf(macierz = graf1.macierz, slownik_kolorow=slownik)
            return nowy_graf

        #return nowy_graf

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
        #self.fitting(self)

    def check(self):
        for x in range(len(self.macierz)):
            for y in range(len(self.macierz)):
                if self.macierz[x][y]:
                    if (self.slownik_kolorow[x + 1] == self.slownik_kolorow[y + 1]):
                        self.szukanie_bledow()
                        print("SASIEDZI MAJA TAKIE SAME KOLORY!",x+1,y+1)
                        print(self.lista_bledow)
                        raise ValueError("Jest problem")
