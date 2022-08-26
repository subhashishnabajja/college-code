import collections

stack = collections.deque([1,2,3,4,5])

print("Stack: ", stack)

# Perform operation from right
print("Pushing 6 on the stack [from right]")
stack.append(6)
print("Stack: ", stack)
print("Poping 6 on the stack [from right]")
stack.pop()
print("Stack: ", stack)

# Perform operation from left
print("Pushing 0 on the stack [from left]")
stack.appendleft(0)
print("Stack: ", stack)
print("Poping 0 on the stack [from left]")
stack.popleft()
print("Stack: ", stack)

