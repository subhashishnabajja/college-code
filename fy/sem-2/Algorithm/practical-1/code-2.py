Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
def infixToPostfix(expression): 
    stack = [] # initialization of empty stack
    output = ''  

    for character in expression:
        if character not in Operators:  
            output+= character
        elif character=='(':  
            stack.append('(')
        elif character==')':

            while stack and stack[-1] != '(':
                output+=stack.pop()
            stack.pop()
    
        else: 
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)

    while stack:
        output+=stack.pop()
        
    return output

expression = input('Enter infix expression ')
print('infix notation: ',expression)
print('postfix notation: ',infixToPostfix(expression))

