import matplotlib.pyplot as plt
'''import csv

x = []
y = []

with open('example.txt', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
'''
import numpy as np

x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x, y, label='loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample graph\n simple plot')
plt.legend()

plt.show()

