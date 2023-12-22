import csv
from collections import Counter

ipalist = []
de_konst_und_vok = ['i', 'y', 'u', 'ɪ', 'e', 'ʏ', 'ø', 'ʊ', 'o', 'ɛ', 'œ', 'ɐ', 'ɔ', 'a',
                    'm', 'n', 'ŋ',
                    'p', 't', 'k','ʔ',
                    'b', 'd', 'ɡ', 
                    'f', 's', 'ʃ', 'ç', 'x', 'h',
                    'v', 'z', 'ʒ', 'j'
                    'l', 'r']

with open("datasets/dewikt.csv", mode='r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for w in reader:
        for l in list(w[1]):
            if l in de_konst_und_vok:
                ipalist += l

with open("output_counts.txt", mode='w',  encoding="utf-8") as output_file:
    for sym, num in Counter(ipalist).items():
        output_file.write(sym + ":" + str(num) + "\n")