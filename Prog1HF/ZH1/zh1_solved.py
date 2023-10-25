cities = ['Budapest', 'Gyor', 'Sopron', 'Szekesfehervar', 'Szombathely', 'Veszprem', 'Zalaegerszeg']

data = {}
for city in cities:
  with open(f'{city}.json') as f:
    import json
    raw = json.load(f)
    days = raw['daily']['time']
    temps = raw['daily']['temperature_2m_max']
    rains = raw['daily']['precipitation_hours']
    winds = raw['daily']['windspeed_10m_max']
    data[city] = {
      'days': days,
      'temps': temps,
      'rains': rains,
      'winds': winds
    }

def question1():
  max_wind = { 'wind': 0 }
  for city in cities:
    wind = data[city]['winds']
    for index in range(len(wind)):
      if wind[index] > max_wind['wind']:
        max_wind = { 'wind': wind[index], 'city': city, 'date': data[city]['days'][index] }

  print(f"Maximális szélsebesség: {max_wind['wind']} km/h, {max_wind['city']}, {max_wind['date']}")

# question1()

def question2():
  rainy_days = 0

  for index in range(len(data['Sopron']['rains'])):
    found = False
    for city in cities:
      if data[city]['rains'][index] >= 1:
        found = True
    if (found):
      rainy_days += 1

  print(f'Csapadékos napok száma: {rainy_days}')

# question2()

def question3():
  temps = []

  for day in range(len(data['Sopron']['days'])):
    max_temp = { 'temp': 0 }
    for city in cities:
      if data[city]['temps'][day] > max_temp['temp']:
        max_temp = { 'temp': data[city]['temps'][day], 'city': city, 'date': data[city]['days'][day] }
    temps.append(max_temp)

  import csv
  with open('max_temp.csv', 'w') as file:
    writer = csv.writer(file)
    for temp in temps:
      writer.writerow([temp['date'], temp['temp'], temp['city']])

# question3()
