def printMultiplicationTable():
    num = int(input("Enter the number: "))
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    for mul in range(start,end+1):
        print(num," x ",mul," = ", num * mul)


if __name__ == "__main__":
    printMultiplicationTable()
