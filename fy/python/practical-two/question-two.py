def calculate_SI():

    # Take the principal value from the user
    principal = int(input("Enter the principal amount\t"))

    #Take the rate of interest from the user
    rate_of_interest = int(input("Enter the rate of interest\t"))

    #Take the number of months from the user
    number_of_months = int(input("Enter the number of months\t"))
    #Convert months into years
    year = number_of_months //12

    #Calculate the interest
    interest =( principal *rate_of_interest * year)/100

    #Show the output to the user
    print("The principal\t",principal)
    print("The rate of interest\t",rate_of_interest)
    print("The number of months\t",number_of_months)
    print("The simple interest is\t",interest)
    print("The total amount is\t",principal+interest)





calculate_SI()
