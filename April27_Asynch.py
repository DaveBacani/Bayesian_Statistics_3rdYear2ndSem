# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:51:22 2024

@author: Dave
"""

import matplotlib.pyplot as plt
import numpy as np

# Simulate some data
np.random.seed(10)  # Set random seed for reproducibility
x = np.linspace(0, 10, 100)
y = 2 * x + 3 + np.random.normal(scale=1, size=100)

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.7, edgecolors='w')  # Adjust alpha for transparency

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of Simulated Data')

# Show the plot
plt.grid(True)
plt.show()