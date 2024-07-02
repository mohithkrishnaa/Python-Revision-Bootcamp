# Seaborn
# Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.
# It is particularly well-suited for visualizing complex datasets and creating aesthetically pleasing plots with minimal code.

import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a simple scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# Scatter Plot
# Scatter plots are used to display the relationship between two numerical variables.
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# Line Plot
# Line plots are used to display data points and the connections between them.
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.show()

# Bar Plot
# Bar plots are used to display the distribution of categorical data.
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()

# Box Plot
# Box plots are used to display the distribution of a dataset and identify outliers.
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# Customizing Plots
# Themes
# You can set the theme of your plots using sns.set_style().
sns.set_style("whitegrid")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# Color Palettes
# Seaborn provides several color palettes that you can use to customize your plots.
sns.set_palette("husl")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# Faceting
# Faceting allows you to create multiple plots based on subsets of your data.
g = sns.FacetGrid(tips, col="time")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()

# Advanced Plotting
# Regression Plots
# Regression plots are used to display the relationship between two variables along with a fitted regression line.
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()

# Joint Plots
# Joint plots combine scatter plots and histograms to show the distribution of two variables.
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.show()

# Pair Grid
# Pair grids allow you to create a grid of plots for pairwise relationships in a dataset.
g = sns.PairGrid(tips)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
plt.show()

# Violin Plot
# Violin plots are used to display the distribution of a dataset across different categories.
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
