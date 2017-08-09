#using CSV module
import matplotlib.pyplot as plt
import csv

x =[]
y= []

with open('example.txt','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		print row
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y,label='Loading data from file')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('practicing visualizing data from file')
plt.legend()

plt.show()