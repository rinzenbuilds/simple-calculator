#simple calculator
num1 = float(input("enter the first number: ")) 
num2 = float(input("enter the second number: ")) 
operation = input("enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(f"the result is: {result}")
