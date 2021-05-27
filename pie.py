import matplotlib.pyplot as plt

slices = [7,3,2,12]
activities = ['sleeping', 'eating', 'working', 'playing']

plt.pie(slices, labels=activities, colors=['m', 'c', 'r', 'green'], shadow=True, explode=(0, 0.1, 0 , 0), autopct='%1.1f%%')

plt.title('Sample graph\n simple plot')

plt.show()

