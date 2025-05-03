def evalRPN(tokens):
    stack = []

    for s in tokens:
        if s in {'*','/','-','+'}:
            b = stack.pop()
            a = stack.pop()

            if s == "+":
                stack.append(a+b)
            
            elif s == "-":
                stack.append(a-b)
            
            elif s == '*':
                stack.append(a * b)
            
            elif s == '/':
                stack.append(int(a/b))
        else:
            stack.append(int(s))
    
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]

print(evalRPN(tokens))