import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

data = pd.read_csv('harleyQuinn.csv')

fig, ax = plt.subplots()

filtered_data = data[(data['Time (s)'] >= 20) & (data['Time (s)'] <= 45)]

# Plot the filtered data
ax.plot(filtered_data['Time (s)'], filtered_data['Linear Acceleration z (m/s^2)'], label='Linear Acceleration z (m/s^2)')

# Calculate the area under the curve between 20 and 45 seconds
area_under_curve = np.trapz(filtered_data['Linear Acceleration z (m/s^2)'], filtered_data['Time (s)'])

# Shade the area under the curve and add legend
ax.fill_between(filtered_data['Time (s)'], filtered_data['Linear Acceleration z (m/s^2)'], alpha=0.3, label='Area under curve', color='C1')

# Set the labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Linear Acceleration z (m/s^2)')

# Add legend
plt.legend()

# Print the area under the curve
print("Area under the curve between 20 and 45 seconds:", area_under_curve)

# Resize the plot
fig.set_size_inches(10, 6)  # width=10 inches, height=6 inches

# Show the plot
plt.show()
