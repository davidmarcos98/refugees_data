import csv
import matplotlib.pyplot as plt
import numpy as np

years_total = {}
suicide = 0
not_known = 0
number = [0, 0, 0, 0, 0, 0]
reasons = ["", "", "", "", "", ""]
with open('tabula-TheList.csv') as File:
    reader = csv.reader(File)
    next(reader)
    for row in reader:
        pos = 1
        year = row[0][-2:]
        if year is "":
            pos = 2
            year = row[1][-2:]
        if "N.N." in row[pos+1]:
            if year not in years_total:
                years_total[year] = row[pos]
            else:
                years_total[year] = int(years_total[year]) + int(row[pos])
        if "suicide" in row[pos+3]:
            reasons[0] = "Suicidio"
            number[0] += int(row[pos])
        elif "drowned" in row[pos+3]:
            reasons[1] = "Ahogamiento"
            number[1] += int(row[pos])
        elif "shot" in row[pos+3]:
            reasons[2] = "Disparo"
            number[2] += int(row[pos])
        elif "missing" in row[pos+3]:
            reasons[3] = "Desaparecidos"
            number[3] += int(row[pos])
        elif "murdered" in row[pos+3]:
            reasons[4] = "Asesinato"
            number[4] += int(row[pos])
        else:
            reasons[5] = "Otros"
            number[5] += int(row[pos])
        if "N.N." in row[pos+1]:
            not_known += int(row[pos])
print (years_total)
total = 0
for year in years_total:
    total = total + int(years_total[year])
print (number)
keys = []
for key in years_total.keys():
    if int(key) < 20:
        keys.append(int("20"+str(key)))
    else:
        keys.append(int("19"+str(key)))

y = years_total.values()
fig = plt.figure()
fig.set_size_inches(8.75, 6)
plt.suptitle("Refugiados 'sin nombre' En Europa entre 1993 y 2018", y=0.95)
plt.plot(keys, y)
plt.figtext(0.6, 0.005, "Data from https://uploads.guim.co.uk/2018/06/19/TheList.pdf", fontsize=8, fontstyle="italic", alpha=0.6)
ax = plt.axes()
plt.yticks(np.arange(0, 4250, step=250))
plt.xticks(keys, rotation="45")
ax.grid(alpha=0.2);
plt.show()

# x = reasons
# y = number
#
# fig = plt.figure()
# fig.set_size_inches(8.75, 8.75)
# plt.suptitle("Razones de fallecimiento:", y=0.95)
# plt.bar(x, y)
# plt.figtext(0.6, 0.005, "Data from https://uploads.guim.co.uk/2018/06/19/TheList.pdf", fontsize=8, fontstyle="italic", alpha=0.6)
# ax = plt.axes()
# plt.yticks(np.arange(0, 22000, step=1500))
# plt.xticks(x, rotation="45")
# ax.grid(alpha=0.2);
# plt.show()

print (total)
print("No names, gender or age info: " + str(not_known))



#Used Tabule (tabula.technology) to extract csv from PDF
#Data thanks to
