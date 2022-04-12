# Selection sort in Python




def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])



data = [int(input("Enter a number: ")) for i in range(int(input("Enter the size of the array: ")))]
print("Unsorted array: ", data)
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)