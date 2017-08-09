import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
		labels = activities,
		colors = cols,
		startangle = 90, #this means that the first division will be a verticle line.
		shadow = True,
		explode =(0,0.1,0,0), # this pops out one slice of the pie chart.
		autopct = '%1.1f%%') # overlays the percentage on the slices.
plt.title('pie chart practice')
plt.show()