import matplotlib.pyplot as plt

# Arrays
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
values = [January_performance, February_performance, March_performance, April_performance, May_performance, June_performance, July_performance, August_performance, September_performance, October_performance, November_performance, December_performance]

# Setting the figure size to accommodate x-axis labels
plt.figure(figsize=(12, 6))

# Plotting
plt.bar(Month, values)

# Setting y-axis limit to 5
plt.ylim(0, 5)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45,ha='right' )

# Labeling
plt.xlabel('Month')
plt.ylabel('Performance')
plt.title('Bar Plot with Limited Y-axis and Rotated X-axis Labels')

# Display the plot
plt.tight_layout()  # Ensures labels and ticks fit within the figure
plt.show()
