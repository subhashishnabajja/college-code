def getSum(end):
    i = 0
    result = i
    while i <= end:
        result += i
        i+=1
        
    return result

end = int(input("Enter the number:"))

print(getSum(end))

