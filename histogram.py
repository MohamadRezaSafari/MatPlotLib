import matplotlib.pyplot as plt

population_ages = [22,55,62,42,42,4,99,21,22,45,102,110,106,113,6,16,17,43,66,73,82,24,31,15,2,104,48,49,51,17,36,28,101]

# ids = [x for x in range(len(population_ages))]
# plt.bar(ids, population_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100,110]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Sample')

plt.show()
