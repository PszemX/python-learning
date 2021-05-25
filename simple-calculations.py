import math

operators = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3
}


def operationToInfix(operation):
    word = ""
    words = []
    for x in range(len(operation)):
        char = operation[x]
        if(char in operators.keys()):
            if(word):
                words.append(word)
                word = ""
            words.append(char)
        elif(char == " "):
            continue
        else:
            word += char
    words.append(word)
    return words


def infixToPostfix(calc):
    stack = []
    output = []
    for x in range(len(calc)):
        char = calc[x]
        if(char.isnumeric()):
            output.append(char)
        elif(char == "("):
            stack.append(char)
        elif(operators[char] > 0):
            if(len(stack) == 0 or operators[char] > operators[stack[len(stack) - 1]]):
                stack.append(char)
            else:
                while(operators[char] <= operators[stack[len(stack) - 1]]):
                    output.append(stack.pop())
                stack.append(char)
        elif(char == ")"):
            while(stack[len(stack) - 1] != "("):
                output.append(stack.pop())
            stack.pop()
        elif(char == " "):
            continue
    while(len(stack) > 0):
        output.append(stack.pop())

    return output


operation = str(input("Enter the math operation: "))
# operation = operation.split()

postfix = infixToPostfix(operationToInfix(operation))
resultStack = []
for i in range(len(postfix)):
    char = postfix[i]
    if(char.isnumeric()):
        resultStack.append(int(char))
    else:
        a = resultStack.pop()
        b = resultStack.pop()
        if(char == "+"):
            resultStack.append(a + b)
        elif(char == "-"):
            resultStack.append(b - a)
        elif(char == "*"):
            resultStack.append(a * b)
        elif(char == "/"):
            resultStack.append(b / a)
        elif(char == "^"):
            resultStack.append(math.pow(b, a))

if (len(resultStack) > 1):
    print("ERROR")
else:
    print(f"Wynik: {resultStack[0]}")
