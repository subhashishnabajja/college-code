# WAP to demonstrate different ways to slice string2) WAP to implement all the methods of class str (String Methods )
#F093 / Subhashish Nabajja

def string_methods():
    example = "Hello world"
    print("Default string:\n",example)
    

    #Capitalize
    print("Capitalize:\n",example.capitalize())
    #Casefold
    print("Casefold: \n",example.casefold())
    #Center
    print("Center: \n",example.center(50,"-"))
    #Count
    print("Count: \n",example.count("Hello"))
    #Encode
    print("Encode: \n",example.encode())
    #Endswith
    print("Endswith: \n",example.endswith("d"))
    #Expand Tabs
    print("Expand Tabs: \n","Hello \t world".expandtabs(10))
    #Find
    print("Find: \n",example.find("world"))
    #Format
    print("Format: \n","This is how {0} {1}".format("formatting","works."))
    #Starts with
    print("Starts with: \n",example.startswith("Hello"))
    #is ASCII
    print("Is ASCII: \n",example.isascii())

  
if __name__ == "__main__":
    string_methods()
