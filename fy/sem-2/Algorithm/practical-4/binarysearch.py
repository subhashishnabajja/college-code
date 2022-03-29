def binarySearch(arr, k, low, high):
   
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:

            low = mid + 1
        else:

            high = mid - 1
    return -1

arr = [int(input("")) for _ in range(int(input("Enter the size of the array")))]

k = 5
result = binarySearch(arr, k, 0, len(arr)-1)

if result != -1:

    print("Element is present at index " + str(result))

else:

    print("Not found")
