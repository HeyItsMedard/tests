#https://matplotlib.org/stable/plot_types/index.html
#ha nincs telepítve, matplotlib extension
import matplotlib.pyplot as plt

pictures = "Testing and Learning\Prog2\matplotlib_pictures"

my_dict={
    1970: 5,
    1980: 7,
    1990: 12,
    2000: 17,
    2010: 14,
    2020: 6
}

"Design (és vonal)"
plt.figure(figsize=(5, 4)) #alakítja a képszélek hosszát, jó resetelésre is
plt.plot(my_dict.keys(), my_dict.values(), marker='o', label="Hepatitis-B") # ide jön vmilyen függvénytípus, megadható neki egy csomó paraméter, ehhez jobb Google
plt.title('Esetszám') # cím
plt.xlabel("Év")
plt.ylabel("Esetek")
plt.yticks(range(min(my_dict.values()), max(my_dict.values())+1)) # rangehez megfelelően egyenként szépen kiírja az eseteket
plt.xticks() # ez csak képletesen szerepel, de az évek már jól néznek itt ki
plt.legend()
plt.tight_layout() # szépítés - automatikus
plt.savefig(f'{pictures}/plotline.png') # mentés
plt.show() #mutat ablakban, futást fenttartja!!!
# Menőbb kinézetért használható: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#Néha az adatok minőségétől, frekvenciájától függ az output kinézete "szépségre" (lásd: oszlopdiagrammok)

"Pontok"
import numpy as np # pip3 install numpy - csak randomnak használom

x_data = np.random.random(50) *100
y_data = np.random.random(50) *100

plt.scatter(x_data, y_data) # pl: x: 24,07, y: 45.7 - koord
plt.savefig(f'{pictures}/scatterdots.png') # mentés
plt.show()

"Oszlopdiagram"
plt.bar(my_dict.keys(), my_dict.values(), color = "r", align="center", width=5)
plt.savefig(f'{pictures}/barvertical.png')
plt.show()

"Sordiagram" # bowling leegyszerűsítve
import random
rounds = list(range(1, 11)) #1-10 kör
eszter = [random.randint(0, 10) for _ in range(10)]
andras = [random.randint(0, 10) for _ in range(10)]
sum_eszter, sum_andras = sum(eszter), sum(andras) #győztes kiszámolásához

bar_width = 0.35

# Szélességek a körhöz mérten
eszter_positions = [round - bar_width / 2 for round in rounds]
andras_positions = [round + bar_width / 2 for round in rounds]

# Színt átállítjuk aszerint, ki győz
eszter_color, andras_color = ('red', 'lightgray') if sum(eszter) > sum(andras) else ('lightgray', 'blue')

plt.barh(eszter_positions, width=eszter, height=bar_width, color=eszter_color, label="Eszter")
plt.barh(andras_positions, width=andras, height=bar_width, color=andras_color, label="Andras")
plt.legend()
plt.xlabel("Pontszám")
plt.ylabel("Kör")
plt.yticks(rounds, range(1, 11))
plt.xticks(list(range(0, 11)), range(11))  
plt.style.use('seaborn-v0_8-bright')
plt.savefig(f'{pictures}/barhorizontal_bowling.png')
plt.show()

"Máté-féle sörivászat, sordiagram"
beer_consumptions = {
    "medard": [2,0,0,1,2,0,2],
    "gergo" : [7,0,7,0,7,0,7],
    "kitti" : [0,1,2,3,4,5,6],
    "iza"   : [6,5,4,3,6,5,4]
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

fig,ax = plt.subplots() # kissé felesleges imo (Medárd)
bottom = [0] * len(days)
for student, beers in beer_consumptions.items():
    print(student, beers)
    print(bottom)
    ax.barh(days,beers,label=student, left=bottom) #y napok, x sörmennyiség, labeling legendnek, értékek stackelése lefttel
    bottom = [bottom[i] + beers[i] for i in range(len(days))] # minden egyes alkalommal hozzáadja az értékeket, hogy egyszerre mennyi sört ittak egyes napokon
    print("Utána ", bottom) # előző sorhoz: pl. hétfő: 0+2, 2+7, 9+0, 9+6 
ax.legend()
fig.savefig(f'{pictures}/barhorizontal_beers.png')

"Hisztogram" # általában folytonosság ábrázolására használjuk, hasonlít az oszlopdiagramra
plt.figure()
data = np.random.randn(1000) #kis számokat generál pl. [ 0.46635556  0.58015853 -0.32655164  1.11889528  0.18271498  0.77808996 -1.63562198 -1.43230758 -0.27550802 -1.3555449 ]
# print(data)
plt.hist(data, bins=10, edgecolor='black', alpha=0.7) # bins az oszlopok száma
plt.savefig(f'{pictures}/histogram.png')
plt.show()

"Kördiagram és textprops"
text_properties = { # ez mindig dictionary
    'color': 'white',
    'fontsize': 12,
    'fontweight': 'bold',
    'backgroundcolor': 'blue',
    'verticalalignment': 'center',
    'horizontalalignment': 'center',
}
langs = {"Python": 50, "C++": 24, "Java": 14, "C#": 6, "C": 17}
plt.pie(list(langs.values()), autopct="%.2f%%", labeldistance=1.1,
        textprops=text_properties) # vagy legend helyett labels
plt.legend(labels=list(langs.keys()))
plt.savefig(f'{pictures}/piechart.png')
plt.show()

"Subplot"

fig, axes = plt.subplots(2, 2) # 2x2-es felület, de lehet üres is

axes[0, 0].plot([1, 2, 3, 4])
axes[0, 1].bar(['A', 'B', 'C'], [3, 6, 1])
axes[1, 0].scatter([1, 2, 3, 4], [3, 1, 2, 4])
axes[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

plt.savefig(f'{pictures}/subplots.png')
plt.show()

# nagyon másra nincs szükség, kivétel ha az Olivér nagyon kreatív akar lenni... ugye Gantt? :) (lásd: HF5)