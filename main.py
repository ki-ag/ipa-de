import csv
from collections import Counter
from matplotlib import pyplot as plt

ipalist = []
de_konst_und_vok = ['i', 'y', 'u', 'ɪ', 'e', 'ʏ', 'ø', 'ʊ', 'o', 'ɛ', 'œ', 'ɐ', 'ɔ', 'a',
                    'm', 'n', 'ŋ',
                    'p', 't', 'k','ʔ',
                    'b', 'd', 'ɡ', 
                    'f', 's', 'ʃ', 'ç', 'x', 'h',
                    'v', 'z', 'ʒ', 'j'
                    'l', 'r']
print("reading csv")

with open("datasets/dewikt.csv", mode='r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for w in reader:
        for l in list(w[1]):
            if l in de_konst_und_vok:
                ipalist += l
print("csv read")

with open("output/counts.txt", mode='w',  encoding="utf-8") as output_file:
    for sym, num in Counter(ipalist).items():
        output_file.write(sym + " " + str(num) + "\n")

print("csv counted and saved in output/")

print("start plotting")
bars = []

with open("output/counts.txt", "r") as file:
    for line in file:
        bar_name, bar_height = line.split()
        bars.append((bar_name, int(bar_height)))
print("read counts.txt")

bars = sorted(bars, key=lambda x: x[1], reverse=True)
print("sorted bars")

bar_names, bar_heights = zip(*bars)

plt.bar(bar_names, bar_heights)

print("saved plot in output/")
plt.savefig("output/plot.png")