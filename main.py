import csv
import matplotlib.pyplot as plt
import numpy as np

# Open the CSV file for reading
with open('StudentsPerformance.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

mathPass = []
mathFail = []

for data in data_list:
    if(int(data["math score"]) > 60):
        mathPass.append(data)
    else:
        mathFail.append(data)


# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
stock_A = [120, 125, 130, 135, 128]
stock_B = [60, 62, 128, 140, 145]
stock_C = [80, 85, 83, 88, 92]
stock_D = [200, 210, 215, 220, 230]

# Setting positions for each bar

# Creating a figure with 4 subplots (2x2 layout)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Subplot 1: Stock A


subjects = ["None", "Completed"]
x1 = np.arange(len(subjects))
axes[0, 0].set_title('Prior Courses')
axes[0, 0].set_xticks(x1)
axes[0, 0].set_xticklabels(subjects)
completed = [data for data in data_list if data["test preparation course"] == "completed"]
none = [data for data in data_list if data["test preparation course"] == "none"]
priorCourse = ['None','Completed']

pasedList = [sum(1 for data in none if int(data["math score"]) > 60), sum(1 for data in completed if int(data["math score"]) > 60)]
failedList = [len(none)-pasedList[0],len(completed)-pasedList[1]] 
axes[0, 0].bar(priorCourse, pasedList, color='g')
axes[0, 0].bar(priorCourse, failedList, bottom=pasedList, color='r')




# Subplot 2: Stock B
# axes[0, 1].bar(x, stock_B, color='orange')
# axes[0, 1].set_title('Stock B')
# axes[0, 1].set_xticks(x)
# axes[0, 1].set_xticklabels(months)

# # Subplot 2: Stock C
# axes[1, 0].bar(x, stock_C, color='green')
# axes[1, 0].set_title('Stock C')
# axes[1, 0].set_xticks(x)
# axes[1, 0].set_xticklabels(months)

# # Subplot 3: Stock D (example extra data)
# axes[1, 1].bar(x, [115, 118, 123, 127, 130], color='skyblue')
# axes[1, 1].set_title('Stock D')
# axes[1, 1].set_xticks(x)
# axes[1, 1].set_xticklabels(months)

# # Add main title and adjust spacing
# fig.suptitle('Monthly Stock Prices', fontsize=16)
# fig.tight_layout(pad=2.0)
plt.show()