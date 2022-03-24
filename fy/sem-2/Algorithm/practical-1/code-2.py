# b. program to find the minimum element in the array



def getMin(array):
    res = array[0]

    for num in array:
        res = min(res, num)
    
    return res

def getMax(array):
    res = array[0]

    for num in array:
        res = max(res, num)
    return res




LIMIT = int(input("Enter the size of the array: "))

array = []

for _ in range(LIMIT):
    array.append(int(input("Enter a number: ")))


print(f"The maximum number is {getMax(array)}")
print(f"The minimum number is {getMin(array)}")