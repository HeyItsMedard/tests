import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from datetime import date
import sys

data = {}
names = {}
countries = []

with open('data.csv') as csvFile:
    reader = csv.reader(csvFile)
    for (country, code, raw_date, cases) in reader:
        date_real = date.fromisoformat(raw_date)
        if code not in data:
            data[code] = { 'date': [date_real], 'cases': [int(cases)] }
            names[code] = country
            countries.append(country)
        else:
            data[code]['date'].append(date_real)
            data[code]['cases'].append(int(cases))


selected = sys.argv[1] if len(sys.argv) >= 2 else 'HUN'

fig, ax = plt.subplots()
# ax.plot(data[selected]['date'], data[selected]['cases'])
ax.plot('date','cases', data=data[selected], label=names[selected])

# for name in names:
#     ax.plot('date','cases', data=data[name], label=names[name])

sub = data[selected]
ym = sub['cases'][:2]
for i in range(2, len(sub['cases'])):
    current = sub['cases'][i]
    prev = sub['cases'][i - 1]
    penu = sub['cases'][i - 2]
    ym.append((current + prev + penu) / 3)
ax.plot(sub['date'], ym, label="Rolling average")

# design improvements?
months = mdates.MonthLocator()
days = mdates.DayLocator()

ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d.'))
fig.autofmt_xdate()
fig.tight_layout()

max_value = 0
for case in data[selected]['cases']:
    if case > max_value:
        max_value = case

max_value = int(len(str(max_value)))
max_value = 10 ** (max_value - 1)

ax.yaxis.set_major_locator(MultipleLocator(max_value))
ax.yaxis.set_minor_locator(MultipleLocator(int(max_value/10)))
ax.yaxis.set_major_formatter('{x:.0f}')

fig.suptitle(f'Daily COVID cases in {names[selected]}')
fig.legend(fontsize="xx-small", ncol=5, loc="upper left")
plt.show()
fig.savefig(f'{selected}.png')
