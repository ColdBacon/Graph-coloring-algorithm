txt=[]      #dane wejściowe z pliku
tablica=[]  #zmiana na int wyjsciowego pliku
slownik={}  #wierzcholek:kolor
n=0         #ilosc wierzcholkow

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

for [x,y] in txt:
    y=int(y)
    x=int(x)
    tablica.append([x,y])
print(tablica)

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
print(slownik)

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
print(TABLICA)

stopnie_wierzcholkow = {}
for x in range(1,n+1):
    stopnie_wierzcholkow[x]=0

for [x,y] in tablica:
    stopnie_wierzcholkow[x]+=1
    stopnie_wierzcholkow[y]+=1

print (stopnie_wierzcholkow)

posortowane_wierzcholki = sorted(stopnie_wierzcholkow.items(), key=lambda x: x[1], reverse=True)
print(posortowane_wierzcholki)

