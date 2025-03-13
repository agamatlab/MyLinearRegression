def isRectangularMatrix(matrix):
    if matrix == []:
        return True
    rows, cols = len(matrix), len(matrix[0]) 
    
    for i in range(1,rows):
        if(len(matrix[i]) != cols) :
            return False

    return True    
    

def transpose2D(matrix):
    if matrix == []:
        return matrix
    
    if not isRectangularMatrix(matrix):
        raise Exception("The matrix has to be rectangular.")
    rows, cols = len(matrix), len(matrix[0]) 

    transposedMatrix = []
    for column in range(cols):
        currentRow = []
        for row in range(rows):
            # print(f'row: {row}, column: {column}, value: {matrix[row][column]}')
            currentRow.append(matrix[row][column])
        transposedMatrix.append(currentRow)
    return transposedMatrix

def sum(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum


def matrixMultipication(matrixA,matrixB):
    if matrixA == [] or matrixB == []:
        raise Exception("Empty Array")
    
    rowsA, colsA = len(matrixA), len(matrixA[0]) 
    rowsB, colsB = len(matrixB), len(matrixB[0])

    if(colsA != rowsB): 
        raise Exception("Matrices cannot be multiplied: Dimensions Mismatch!\n"
                        + f"colsA({colsA}) != rowsB({rowsB})")

    if not isRectangularMatrix(matrixA) or not isRectangularMatrix(matrixB):
        raise Exception("The matrices has to be rectangular.")
    
    result = []
    for rowA in range(rowsA):
        currentRow = []
        for colB in range(colsB):
                product = [ float(matrixA[rowA][index]) * float(matrixB[index][colB]) for index in range(colsA)]
                currentRow.append(sum(product))
        result.append(currentRow)
            
    return result

def createIdentity(n):
    result = []
    for i in range(n):
        currentRow = []
        for j in range(n):
            currentRow.append(0)
        currentRow[i] = 1
        result.append(currentRow)
    return result

def concatenateMatrices(matrixA, matrixB):
    result = []
    n = len(matrixA)

    for i in range(n):
        result.append(matrixA[i]+matrixB[i])
    return result

def splitColumns(matrix, columnIndex):
    resultA = []
    resultB = []
    rowCount, columnCount = len(matrix), len(matrix[0])

    for i in range(rowCount):
        rowA = []
        rowB = []
        for k in range(columnIndex):
            rowA.append(matrix[i][k])
        for k in range(columnIndex, columnCount):
            rowB.append(matrix[i][k])
        resultA.append(rowA)
        resultB.append(rowB)

    return resultA, resultB



def inverse(matrix):
    n = len(matrix)
    I = createIdentity(n)

    augmented = concatenateMatrices(matrix, I)
    for i in range(n):
        if augmented[i][i] ==  0:
            for j in range(i+1,n):
                if augmented[j][i] != 0:
                    # Swap these two rows
                    temp = augmented[i]
                    augmented[i] = augmented[j]
                    augmented[j] = temp
                    break
    
        pivot = augmented[i][i]
        for k in range(0,2*n):
            augmented[i][k] = augmented[i][k] /pivot
        
        for j in range(0,n):
            if j != i:
                factor = augmented[j][i]
                for k in range(2*n):
                    augmented[j][k] = augmented[j][k] - factor * augmented[i][k]
    
    _, A_inv = splitColumns(augmented, n) 
    return A_inv



