import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,10,9,7]
eating = [2,3,1,4,2]
working = [7,8,4,2,5]
playing = [8,5,9,8,10]

plt.plot([], [], color='m', label='sleeping', linewidth=5)
plt.plot([], [], color='c', label='eating', linewidth=5)
plt.plot([], [], color='r', label='working', linewidth=5)
plt.plot([], [], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Sample')

plt.show()
