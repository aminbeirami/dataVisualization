import matplotlib.pyplot as plt

populationAges = [55,33,12,15,17,18,37,29,40,45]
bins = [10,20,30,40,50,60]

plt.hist(populationAges,bins,histtype = 'bar', rwidth = 1)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('histogram practice')

plt.show()