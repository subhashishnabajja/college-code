try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    print(n1 + n2)
except:
    print("Something went wrong")
else:
    print("Added two numbers")
finally:
    print("Exiting...")