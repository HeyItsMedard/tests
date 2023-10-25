import json
#1.
varosok = ["Sopron", "Gyor", "Szombathely", "Budapest", "Veszprem", "Szekesfehervar", "Zalaegerszeg"]
maxwind = 0
measure = None
maxidx = 0
maxlocation = None
maxdate = None
for varos in varosok:
    with open(f"{varos}.json") as j:
        data = json.load(j)
        for key, values in data.items():
            if key == "daily":
                for key2, values2 in values.items():
                    if key2 == "windspeed_10m_max":
                        idx = 0
                        for speed in values2:
                            idx += 1
                            if speed>maxwind:
                                maxwind =speed
                                maxlocation = varos
                                maxidx = idx
                    if key2 == "time":
                        maxdate = values2[maxidx-1]
print(f"Maximális szélsebesség: {maxwind} km/h, {maxlocation}, {maxdate}")

#2.
getrainydays = []
#days = [0]*31
for varos in varosok:
    with open(f"{varos}.json") as j:
        data = json.load(j)
        for key, values in data.items():
            if key == "daily":
                for key2, values2 in values.items():
                    if key2 == "precipitation_hours":
                        getdateidx = 1
                        for rain in values2:
                            if rain >= 1.0 and getdateidx not in getrainydays:
                                getrainydays.append(getdateidx)
                            getdateidx+=1
print("Csapadékos napok száma:", len(getrainydays))

#3.
#ido, hom, hely ;-vel elválasztva
maxlist = [0] *31
maxvaros = [0] *31
for varos in varosok:
    with open(f"{varos}.json") as j:
        data = json.load(j)
        with open("max_temp.csv", "w") as w:
            for key, values in data.items():
                if key == "daily":
                    for key2, values2 in values.items():
                        if key2 == "temperature_2m_max":
                            i=0
                            for temp in values2:
                                if temp > maxlist[i]:
                                    maxlist[i] = temp
                                    maxvaros[i] = varos
                                i+=1
                        if key2 == "time":
                            i = 0
                            for date in values2:
                                w.write(f"{date};")
                                w.write(f"{maxlist[i]};")
                                w.write(f"{maxvaros[i]}\n")
                                i+=1
