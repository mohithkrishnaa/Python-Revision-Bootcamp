# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations. 
# It is highly customizable and can produce a wide range of plot types.

import matplotlib.pyplot as plt

# BASIC LINE PLOT
# Sample data
x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 15]

# Create a line plot
plt.plot(x, y, label='Line 1', color='blue', marker='o')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# SCATTERPLOT
# Sample data
x = [1, 2, 3, 4, 5]
y = [4, 1, 8, 10, 6]

# Create a scatter plot
plt.scatter(x, y, color='red')

# Add title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()

# BAR CHART 
# Sample data
categories = ['X', 'Y', 'Z', 'W']
values = [20, 34, 30, 35]

# Create a bar chart
plt.bar(categories, values, color='green')

# Add title and labels
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()

# PIE CHART
# Sample data
labels = ['X', 'Y', 'Z', 'W']
sizes = [25, 35, 20, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode the 1st slice (X)

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Simple Pie Chart')

# Show the plot
plt.show()
