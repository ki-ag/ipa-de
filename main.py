import csv
from collections import Counter
from matplotlib import pyplot as plt
import os

de_konst_und_vok = ['i', 'y', 'u', 'ɪ', 'e', 'ʏ', 'ø', 'ʊ', 'o', 'ɛ', 'œ', 'ɐ', 'ɔ', 'a',
                    'm', 'n', 'ŋ',
                    'p', 't', 'k', 'ʔ',
                    'b', 'd', 'ɡ',
                    'f', 's', 'ʃ', 'ç', 'x', 'h',
                    'v', 'z', 'ʒ', 'j'
                    'l', 'r']

csv_folder = "datasets/"
output_folder = "output/"

for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        data = os.path.join(csv_folder, csv_file)
        ipalist = []

        print(f"Reading CSV: {data}")

        with open(data, mode='r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for w in reader:
                for l in list(w[1]):
                    if l in de_konst_und_vok:
                        ipalist += l

        output_filename = f"{csv_file.split('.')[0]}_counts.txt"

        with open(os.path.join(output_folder, output_filename), mode='w', encoding="utf-8") as output_file:
            for sym, num in Counter(ipalist).items():
                output_file.write(sym + " " + str(num) + "\n")

        print(f"CSV counted and saved in {output_filename}")

        print("Start plotting")
        bars = []

        with open(os.path.join(output_folder, output_filename), "r") as file:
            for line in file:
                bar_name, bar_height = line.split()
                bars.append((bar_name, int(bar_height)))

        # bars = sorted(bars, key=lambda x: x[1], reverse=True)

        bar_names, bar_heights = zip(*bars)

        plt.title(csv_file)
        plt.bar(bar_names, bar_heights)

        plt.savefig(os.path.join(output_folder, f"{csv_file.split('.')[0]}_plot.png"))
        plt.clf()  # Clear the current figure to start a new one for the next iteration

        print(f"Saved plot in {output_folder}/{csv_file.split('.')[0]}_plot.png")
