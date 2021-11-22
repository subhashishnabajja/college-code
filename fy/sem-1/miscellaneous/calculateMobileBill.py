def calculateCharge(serviceUsed, limit, rate ):
    '''The calculateCharge function takes the number of calls/messages, free-tier limit and rate as arguments and return the calculate charge'''
    charge = 0
    if serviceUsed > limit:
        charge = (serviceUsed - limit) * rate

    return charge

def withGST(amount , rate ):
    '''Return the amount with appropriate GST rate'''
    return amount * rate /100

def generateMobileBill ():
    ''' Generate the user's mobile name. The function accepts user's name, total calls and total
        messages /The basic rental of the service is Rs. 300 which includes 50 calls and 100
        messages. After the free tier the call rates are Rs. 2 / call and Rs.1 / message
    '''
    
    #Constants
    BASE_CHARGE = 300
    BASE_CALL_LIMIT = 50
    CHARGE_PER_CALL = 2
    BASE_MESSAGE_LIMIT = 100
    CHARGE_PER_MESSAGE = 1
    

    # Take the inputs from the user
    userName = input("Enter your name: ")
    totalCalls = int(input("Enter the number of calls that you have made : "))
    totalMsgs = int(input("Enter the number of message that you have send : "))

    #Validating the input
    if totalCalls < 0 or totalMsgs < 0:
        print("Invalid data")
        return generateMobileBill()

    # Calculating the charges for calls and messages
    callCharge = calculateCharge(totalCalls,BASE_CALL_LIMIT,CHARGE_PER_CALL )
    msgCharge = calculateCharge(totalMsgs,BASE_MESSAGE_LIMIT,CHARGE_PER_MESSAGE)

    total = BASE_CHARGE+callCharge+msgCharge

    # Start printing the invoice
    print("--"*5 , " INVOICE " ,"--"*5)
    print("Consumer name : " , userName)
    print("Calls made :" , totalCalls )
    print("Calls made :" , totalMsgs )
    print("Base charge\t", BASE_CHARGE )
    print("Calls charge\t", callCharge )
    print("Message charge\t", msgCharge )
    print("GST @18%\t", withGST(total,18))
    print("Total", total + withGST(total,18))
    print("--"*5 , " END INVOICE " ,"--"*5)
    
    
    
generateMobileBill()
