from matplotlib import pyplot as plt

bars = []

with open("output/counts.txt", "r") as file:
    for line in file:
        bar_name, bar_height = line.split()
        bars.append((bar_name, int(bar_height)))

bars = sorted(bars, key=lambda x: x[1], reverse=True)

bar_names, bar_heights = zip(*bars)

plt.bar(bar_names, bar_heights)

plt.savefig("output/plot.png")