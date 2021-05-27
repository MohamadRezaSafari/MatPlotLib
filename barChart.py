import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label = 'bars1', color='red')
plt.bar(x2, y2, label = 'bars2', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Sample graph\n simple plot')

plt.show()

