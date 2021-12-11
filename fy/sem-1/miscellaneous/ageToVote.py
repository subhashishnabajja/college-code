def agetovote(): 
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible for voting")
    elif age < 18 and age >0:
        print("You are not eligible for voting")
    else: 
        print("Incorrect age value")
        print("Please try again")
        agetovote()

agetovote()
