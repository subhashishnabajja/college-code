# Program to create a list-based stack and perform various stack operations. 
print("F093 / Subhashish Nabajja")

stack = []


stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("Initial Stack: ", stack)



for _ in range(len(stack)):
    print(f"{stack.pop()} popped from the stack")

print("Final stack: ", stack)