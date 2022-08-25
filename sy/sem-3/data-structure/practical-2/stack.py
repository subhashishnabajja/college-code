class Stack():

    def __init__(self, size, initial = []):
        self.stack = initial
        self.size = size

    def stack(self):
        return self.stack

    def push(self, data): 
        if self.isFull():
            return
        self.stack.append(data)
    
    def pop(self):
        if self.isEmpty():
            return print("Stack is empty")

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return True if len(self.stack) is 0 else False

    def isFull(self):
        return True if len(self.stack) == self.size else False        



if __name__ == "__main__":
    stack = Stack(3)

    print("Push 1 : ", stack.push(1))
    print("Push 2 : ", stack.push(2))
    print("Stack : ", stack.stack)
    print("Pop : ", stack.pop())
    print("Pop : ", stack.pop())
    print("Pop : ", stack.pop())
    print("Pop : ", stack.pop())
    print("Stack : ", stack.stack)