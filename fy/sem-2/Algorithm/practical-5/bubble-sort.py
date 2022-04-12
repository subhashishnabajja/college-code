lst = []

n = int(input("Number of elements of array: "))

for _ in range(n):
    lst.append(int(input("Enter a elemennt in a array")))

print("Entered array :", lst)

for x in range(len(lst)):
    for y in range(len(lst) - x - 1):
        if lst[y] > lst[y + 1]:
            temp = lst[y]
            lst[y] = lst[y + 1]
            lst[y + 1] = temp

print("Sorted array: ", lst)
