import csv
from collections import Counter
from matplotlib import pyplot as plt
import os

ipa_sym = [ 
            'p','b','t','d','c','k','ɡ','q','m','n','r','f','v','s','z','x','h','j','l','i','y','u','e','o','a',
            'ɑ','æ','ɐ','β','ɓ','ʙ','ç','ɕ','ð','ɖ','ɗ','ə','ɚ','ɵ','ɘ','ɛ','ɜ','ɝ','ɞ','ɠ','ɢ','ʛ','ɡ','ħ','ɦ',
            'ɥ','ɧ','ʜ','ɪ','ɨ','ʝ','ɟ','ʄ','ɫ','ɭ','ɬ','ʟ','ɮ','ɱ','ŋ','ɲ','ɳ','ɴ','ɔ','œ','ɒ','ɶ','ø','ɸ','ɾ',
            'ɹ','ʁ','ʀ','ɻ','ɽ','ɺ','ʃ','ʂ','θ','ʈ','ʊ','ʉ','ʌ','ʋ','ⱱ','ɯ','ʍ','ɰ','χ','ʎ','ʏ','ɤ','ʒ','ʐ','ʑ',
            'ʔ','ʕ','ʡ','ʢ','ǀ','ǁ','ǂ','ǃ','ʘ','ʩ','ʪ','ʫ','ꞎ','ʬ','ʭ','¡', 
            '\u0361', '\u035d', '\u035c'
          ]

csv_folder = "datasets/"
output_folder = "output/"
skip = 0
percent = 0

for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        data = os.path.join(csv_folder, csv_file)
        ipalist = []

        print(f"Reading CSV: {data}")

        with open(data, mode='r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for w in reader:
                for l in range(len(list(w[1]))-1):
                    if list(w[1])[l] in ipa_sym:
                        if list(w[1])[l+1] == '\u0361' or list(w[1])[l+1] == '\u035d' or list(w[1])[l+1] =='\u035c':
                            ipalist.append(list(w[1])[l] + list(w[1])[l+1] + list(w[1])[l+2])
                            skip = 3
                        if skip > 0:
                            skip -= 1
                            continue
                        ipalist += list(w[1])[l]
                
        output_filename = f"{csv_file.split('.')[0]}_counts.txt"

        with open(os.path.join(output_folder, output_filename), mode='w', encoding="utf-8") as output_file:
            for sym, num in Counter(ipalist).items():
                procent = num / len(ipalist)
                output_file.write(f"{sym} {num} {percent}\n")

        print(f"CSV counted and saved in {output_filename}")

        print("Start plotting")
        bars = []

        with open(os.path.join(output_folder, output_filename), mode="r", encoding="utf-8") as file:
            for line in file:
                bar_name, bar1_height, bar2_height = line.split()
                bars.append((bar_name, int(bar1_height)))

        bars = sorted(bars, key=lambda x: x[1], reverse=True)

        bar_names, bar_heights = zip(*bars)

        plt.title(csv_file)
        plt.bar(bar_names, bar_heights)

        plt.savefig(os.path.join(output_folder, f"{csv_file.split('.')[0]}_plot.png"))
        plt.clf()  # Clear the current figure to start a new one for the next iteration

        print(f"Saved plot in {output_folder}/{csv_file.split('.')[0]}_plot.png")
