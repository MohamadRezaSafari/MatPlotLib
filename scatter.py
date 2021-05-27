import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,4,3,2,5,3,4,2]

plt.scatter(x, y, label = 'test', color = 'red', s=100, marker='*')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample')

plt.show()
