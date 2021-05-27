import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,8]

plt.plot(x, y, label = 'firstName')
plt.plot(x2, y2, label = 'second line')

plt.xlabel('Plot Number')
plt.ylabel('Variation')
plt.legend()
plt.title('Sample')

plt.show()

# plt.plot([1,2,3],[5,7,4])
# plt.show()