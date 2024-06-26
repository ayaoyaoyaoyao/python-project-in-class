# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:49:41 2024

@author: yiyao
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=20)

#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()