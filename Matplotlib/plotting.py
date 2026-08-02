import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#this plots a simple line graph with x and y values
plt.plot(x, y)

#this plots a bar graph with x and y values
plt.bar(x, y)

#this plots a scatter plot with x and y values
plt.scatter(x, y)

#this plots a pie chart with x and y values
plt.pie(y, labels=x)

plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()