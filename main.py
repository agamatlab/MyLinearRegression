import csv
from visualization import showFigure

# Open the CSV file for reading
with open('StudentsPerformance.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

showFigure(data_list)