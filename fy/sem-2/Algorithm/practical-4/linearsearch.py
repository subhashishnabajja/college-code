COUNT = int(input("Enter the number of the elements"))

array = [ ]

print("Enter the number of elements")
for _ in range(COUNT):
    array.append(int(input("")))

def linearSearch(array, target):

    for i in range(len(array)):
        if array[i] == target: return i


print(linearSearch(array, target=5))