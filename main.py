import csv
from visualization import showFigure
from encoding import encode_OneShot
from matrix_operations import *
from helper import *

# Open the CSV file for reading
with open('StudentsPerformance.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

### Show the figure with pass/fail rate

# showFigure(data_list)


### Numeralization to turn categorical data in to 0s and 1s
categoricalFeatures = ["gender","race/ethnicity","parental level of education","test preparation course", "lunch"]
numericalFeautes = ["writing score", "reading score"]
numerializedData = encode_OneShot(categoricalFeatures,numericalFeautes, data_list)

### Finding vector of coefficients
target = "math score"
numerializedArray = dictionary_to_list(numerializedData)
y = transpose2D([ [data[target] for data in data_list ] ])
# (X^T @ X)
coefficients = matrixMultipication(transpose2D(numerializedArray), numerializedArray)
# (X^T @ X)^-1
coefficients = inverse(coefficients)
# (X^T @ X)^-1 @ X^T
coefficients = matrixMultipication(coefficients, transpose2D(numerializedArray))
# (X^T @ X)^-1 @ X^T^ y
coefficients = matrixMultipication(coefficients, y)

print(coefficients)