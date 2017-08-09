import matplotlib.pyplot as plt

x = [3,5,9,8,4]
y = [5,8,1,6,7]

plt.scatter(x,y, label = 'random data', color = 'k', s=25, marker= 'o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('scatter plot practice')
plt.legend()

plt.show() 