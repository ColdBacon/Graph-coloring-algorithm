import random,math

file = open("proba.txt","w")
#ilosc_wierzcholkow=random.randint(5,10)
ilosc_wierzcholkow=150
gestosc=0.3
matryca=[[0 for x in range(ilosc_wierzcholkow)]for y in range(ilosc_wierzcholkow)]
for x in range(ilosc_wierzcholkow-1):
    matryca[x][x+1]=1
    matryca[x+1][x]=1
ilosc_krawedzi=math.floor(((ilosc_wierzcholkow*(ilosc_wierzcholkow-1))/2*gestosc)-ilosc_wierzcholkow+1)
print(ilosc_krawedzi)
while(ilosc_krawedzi>0):
    x=random.randint(0,ilosc_wierzcholkow-1)
    y=random.randint(0,ilosc_wierzcholkow-1)
    if x==y or matryca[x][y]==1:
        continue
    else:
        matryca[x][y]=1
        matryca[y][x]=1
        ilosc_krawedzi-=1

for x in matryca:
    print(x)
print(ilosc_krawedzi)
file.write(str(ilosc_wierzcholkow))
file.write("\n")
for x in range(ilosc_wierzcholkow):
    for y in range(ilosc_wierzcholkow):
        if x<y:
            if matryca[x][y]:
                wynik=str(x+1)+' '+str(y+1)
                file.write(wynik)
                file.write("\n")

file.close()
