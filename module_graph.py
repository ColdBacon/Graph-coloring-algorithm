#!/usr/bin/python3

def max_slownik(slownik):      #zwraca ilosc kolorow
    maxi=0
    for x in slownik.values():
        if x>maxi:
            maxi=x
    return maxi

class Graf:         #klasa graf przechowuje pokolorowane wierzcholki grafu

    lista_grafow = []           #lista przechowuje wszystkie pokolorowania (slowniki) w populacji (pole statyczne)

    def kolorowanie(self):       #funkcja kolorujaca zachlannie i zwracajaca slownik {indeks_wierzcholka:numer_koloru}
        lista_wychodzacych=[]   #lista z wierzcholkami polaczonymi z jednym wierzcholkiem do którego dobieramy kolor
        slownik_kolorow={}
        for i in range(1,len(self.lista_krawedzi)+1):
            slownik_kolorow[i]=0
        kolor=0                 #numery oznaczają kolory
        for i in self.lista_krawedzi:
            for [x,y] in self.macierz:
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
    
    def __init__(self,macierz,lista_krawedzi):      #inicjalizacja grafu
        self.macierz = macierz
        self.lista_krawedzi = lista_krawedzi
        self.slownik_wierzcholkow = self.kolorowanie()      #kolorowanie grafu
        Graf.lista_grafow.append(self.slownik_wierzcholkow) #dodawanie slownikow do listy

    def max_z_slownika(self):      #zwraca ilosc kolorow
        maxi=0
        for x in self.slownik_wierzcholkow.values():
            if x>maxi:
                maxi=x
        return maxi

    @staticmethod
    def odrzucanie_populacji():
        Graf.lista_grafow = Graf.lista_grafow[0:len(Graf.lista_grafow)//2]
    
    @staticmethod 
    def sortowanie_populacji():
        Graf.lista_grafow.sort(key=max_slownik)
