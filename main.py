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

print(len(mathPass))
print(len(mathFail))


# Sample data
subjects = ["None", "Completed"]
stock_A = [120, 125, 130, 135, 128]
stock_B = [60, 62, 128, 140, 145]
stock_C = [80, 85, 83, 88, 92]
stock_D = [200, 210, 215, 220, 230]

completed = [data for data in data_list if data["test preparation course"] == "completed"]
none = [data for data in data_list if data["test preparation course"] == "none"]
priorCourse = ['None','Completed']

pasedList = [sum(1 for data in none if int(data["math score"]) > 60), sum(1 for data in completed if int(data["math score"]) > 60)]
failedList = [1000-value for value in pasedList] 
plt.bar(priorCourse, pasedList, color='g')
plt.bar(priorCourse, failedList, bottom=pasedList, color='r')
plt.title('Prior Courses')
plt.xlabel('Prior Courses')
plt.ylabel('Count')
plt.show()


