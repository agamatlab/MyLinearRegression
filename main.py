import csv
import matplotlib.pyplot as plt
import numpy as np

# Open the CSV file for reading
with open('StudentsPerformance.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

mathPass = 0
mathFail = 0

for data in data_list:
    if(int(data["math score"]) > 60):
        mathPass += 1
    else:
        mathFail += 1

print(mathPass)
print(mathFail)


# # Sample data
# subjects = ['Math', 'Reading', 'Writing']
# stock_A = [120, 125, 130, 135, 128]
# stock_B = [60, 62, 128, 140, 145]
# stock_C = [80, 85, 83, 88, 92]
# stock_D = [200, 210, 215, 220, 230]



# # Setting positions for each bar
# x = np.arange(len(subjects))

# # Creating a figure with 4 subplots (2x2 layout)
# fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# # Subplot 1: Stock A
# axes[0, 0].bar(x, stock_A, color='skyblue')
# axes[0, 0].set_title('Test Preparation Course')
# axes[0, 0].set_xticks(x)
# axes[0, 0].set_xticklabels(subjects)

# axes[0, 0].bar(x - 0.2, , 0.4, label = 'Pass') 
# axes[0, 0].bar(x + 0.2, Zboys, 0.4, label = 'Fail') 

# # Subplot 2: Stock B
# axes[0, 1].bar(x, stock_B, color='orange')
# axes[0, 1].set_title('Stock B')
# axes[0, 1].set_xticks(x)
# axes[0, 1].set_xticklabels(subjects)

# # Subplot 2: Stock C
# axes[1, 0].bar(x, stock_C, color='green')
# axes[1, 0].set_title('Stock C')
# axes[1, 0].set_xticks(x)
# axes[1, 0].set_xticklabels(subjects)

# # Subplot 3: Stock D (example extra data)
# axes[1, 1].bar(x, [115, 118, 123, 127, 130], color='skyblue')
# axes[1, 1].set_title('Stock D')
# axes[1, 1].set_xticks(x)
# axes[1, 1].set_xticklabels(subjects)

# # Add main title and adjust spacing
# fig.suptitle('Monthly Stock Prices', fontsize=16)
# fig.tight_layout(pad=2.0)
# plt.show()
