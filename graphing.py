from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

bar_names = []
bar_heights = []

with open("output/counts.txt", "r") as file:
    for line in file:
        bar_name, bar_height = line.split()
        bar_names.append(bar_name)
        bar_heights.append(int(bar_height))

plt.bar(bar_names, bar_heights)

plt.savefig("output/plot.png")