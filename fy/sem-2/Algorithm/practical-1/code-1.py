# Program to find sum of elements in an array

SIZE = int(input("Enter the numbers of elements in the array: "))

array = []


for i in range(SIZE):
    array.append(int(input("Enter a number: ")))


print(f"The sum of the elements in the array is: {sum(array)} ")
