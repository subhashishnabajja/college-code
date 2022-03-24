#  c.Python3 program to count number of even and odd elements in an array



SIZE = int(input("Enter the size of the array: "))

array  = []

for _ in range(SIZE):
    array.append(int(input("Enter a number: ")))

count = {
    "odd": 0,
    "even": 0
}

for num in array:
    
    if num % 2 == 0:
        count["even"] += 1
    else:
        count["odd"] += 1


print("The number of odd numbers are ",count["odd"])
print("The number of even numbers are ",count["even"])