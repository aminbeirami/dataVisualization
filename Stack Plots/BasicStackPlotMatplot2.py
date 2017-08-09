import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,6,11,7,5]
eating = [2,3,2,4,2]
working = [7,6,3,5,8]
playing = [8,9,8,8,9]

plt.plot([],[], color = 'm', label='sleeping',linewidth = 5)
plt.plot([],[], color = 'c', label = 'eating',linewidth = 5)
plt.plot([],[], color = 'r', label= 'working', linewidth = 5)
plt.plot([],[], color = 'k', label = 'playing', linewidth = 5)
plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','c','r','k'])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('stack plot practice')
plt.legend()

plt.show()