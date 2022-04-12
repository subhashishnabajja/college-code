def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
    
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            
        array[j + 1] = key


data = [int(input("Enter a number: ")) for i in range(int(input("Enter the size of the array: ")))]

print("Unsorted array: ", data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)