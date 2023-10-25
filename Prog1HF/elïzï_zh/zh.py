import random
def sorsol(elso, utolso):#kisorsolja nyerő számok listáját
    szamok=[]
    szam=random.randint(elso,utolso)
    while len(szamok)!=5:
        if szam not in szamok:
            szamok.append(szam)
        szam=random.randint(elso,utolso)

    return szamok 
nyeroszamok=sorsol(1,20)
#nyeroszamok=[3,10,13,9,14]

import json
with open('./előző_zh/szelvenyek.json') as file:#json file beolvasása
    szelvenyek=json.load(file)
nevek={}
#print(szelvenyek)
nyeremeny=[]
with open ("./előző_zh/nyeremeny.txt") as file2:#nyeremeny.txt file beolvasása és bele teszi a nyeremény listába
    for line in file2:
        nyeremeny+=line.split()
#print(nyeremeny)


def kiertekel(szelveny,nyeroszamok):#megszámolja hogy a szelvényen hány találat van
    db=0
    for szam in szelveny:
        if szam in nyeroszamok:
            db+=1
    return db
nyertesek={}
talalatok2=[0]*5# létrehozza a találatok listáját és feltölti nullával hogy ha nincs 5 ös találat akkor is 5 elemű legyen a lista

for lista in szelvenyek:# léétrehozza a nevek dicktet amiben 
    for kulcs,ertek in lista.items():
        nevek[lista["nev"]]=lista["szelvenyek"]
talalatoksz=[]
#print(nevek)
for nev, szelvenylist in nevek.items():# letrehozza a nyertesek dict-jét
    for szelveny in szelvenylist:
        db=kiertekel(szelveny,nyeroszamok)# meg adja hány db találat van az adott szelvényen 
        if db >1:
            if nev in nyertesek:
                nyertesek[nev]+=int(nyeremeny[db])

            else:
                nyertesek[nev]=int(nyeremeny[db])
        if db>=1: #megvizsgálja a db-t ha nagyobb mint 1 akkor a találatok list megfelelő indexét nőveli egyel igy megkapom hogy bizonyos találatokból hány db van
            db-=1
            talalatok2[db]+=1
print(talalatok2)  
#print()
#print(nyertesek)              

with open ("./előző_zh/nyertesek2.txt","w") as irtf:#kiirja nyertesek2.txtbe a nyertesek listáját
    for nev, penz in nyertesek.items():
        irtf.write(f"{nev} {penz}Ft"'\n')
#print(nyertesek)


def kiiratas(nyeroszamok,talalatok):# Kiiratom az eredményeket a terminálba ez jó
    print("A mai nyerőszámok: ", end="")
    for i in nyeroszamok: 
        print(i,end=" ")
    print("")
    j=5
    while j>1:
        print(f"{talalatok2[j-1]} db {j}-találatokszelvény")
        j-=1
kiiratas(nyeroszamok,talalatok2)