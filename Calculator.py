# Simple Calculator
number = True
while number:
    number = float(input("Input a number: "))
    operation = input("+, -, *, or /: ")
    number2 = float(input("Input another number: "))
    if operation == '+':
        print(f"Result: {number + number2}")  
    elif operation == '-':
        print(f"Result: {number - number2}")        
    elif operation == '*':
        print(f"Result: {number * number2}")        
    elif operation == '/':
        print(f"Result: {number / number2}")
    else:
        print("Syntax Error: Cannot Compute.")
