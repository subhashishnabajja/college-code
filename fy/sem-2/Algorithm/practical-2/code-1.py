from tkinter.tix import COLUMN
import numpy as np
# get array input

def getArray():
    ROW = int(input("Enter the number of rows: "))
    COLUMN = int(input("Enter the number of columns: "))

    array = []

    for _ in range(ROW):
        row = []
        for _ in range(COLUMN):
            row.append(int(input("Enter a number: ")))
        array.append(row)

    return np.array(array)


def getRowSum(array):
    ROW, COLUMN = array.shape

    for i in range(ROW):
        sum = 0

        for j in range(COLUMN):
            sum += array[i][j]

        print(f"The sum for row {i+1} is {sum}")




def getColSum(array):
    ROW, COLUMN = array.shape

    for i in range(COLUMN):
        sum = 0

        for j in range(ROW):
            sum += array[j][i]

        print(f"The sum of the {i + 1} column is {sum}")
        


def getDiagonalSum(array):
    ROW, COLUMN = array.shape

    if ROW != COLUMN:
        return print("[Error] Expected a square matrix")

    sum = 0
    for i in range(ROW):
        for j in range(COLUMN):

            if i == j:
                sum += array[i][j]

    print(sum)


def getSecondaryDiagonalSum(array):
    ROW, COLUMN = array.shape

    if ROW != COLUMN:
        return print("[Error] Expected a square matrix")

    sum = 0
    for i in range(ROW):
        for j in range(COLUMN):

            if (i + j + 1) == ROW:
                sum += array[i][j]
    print(sum)


def addTwoMatrix(arrayOne, arrayTwo):

    if arrayOne.shape != arrayTwo.shape:
        print("[Error] The entered matrix are not similar")
    ROW, COLUMN = arrayOne.shape

    result = []

    for i in range(ROW):
        row = []
        for j in range(COLUMN):
            row.append(arrayOne[i][j] + arrayTwo[i][j])

        result.append(row)

    print(np.array(result))



def matrixMultiplication(arrayOne, arrayTwo):

    ROW, _ = arrayOne.shape
    _ ,COLUMN = arrayTwo.shape

    result = []

    for i in range(ROW):
        row = [0 for i in range(ROW) ]
        print(row)

        for j in range(COLUMN):
            
            for k in range(arrayTwo.shape[1]):
                row[k] += arrayOne[i][k] * arrayTwo[k][j] 

        result.append(row)

    print(result)


matrixMultiplication(getArray(), getArray())