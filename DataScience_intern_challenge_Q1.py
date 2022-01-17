#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:10:57 2022

@author: rafaellacorrea
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('~/workspace/Shopify/Data Science/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv')

total = data['order_amount']
items = data['total_items'].sum()

total.hist(bins = 20)
plt.show()

mode = int(total.mode())
mean = total.mean()
med = total.median()

print("The mode is", mode)
print("The mean is", mean)
print("The median is", med ,"\n")

# These measures are very distinct and we can see that the mean is above where the histogram indicates most of the values are in
# This means we have outliers, increasing the AOV
# Checking the amounts under 3000, with most of the values
avg = total[total <= 3000]
avg_count = avg.count()
outliers = total[total > 3000]
outliers_count = outliers.count()

avg.mean()
outliers.mean()

print("Most of the order amounts are between", avg.min(), "and", avg.max(),"where we can find", avg_count, "values in it.\n")
print("Meaning we have", outliers_count, "outliers values increasing the AOV, between", outliers.min(), "and", outliers.max(), "\n")

actual_AOV = (data['order_amount'].sum())/items

print("The actual AOV (average of values) is", actual_AOV, "and we have it when we divide the total order amount by the total items sold.")