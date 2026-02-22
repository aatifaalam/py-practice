# Make a calculator that can be basic operations like addition, subtraction, multiplication, and divider

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operation = input("Enter the operation symbol: ")
if operation == "+":
    print("The result of addition is: ", a + b)
elif operation == "-":
    print("The result of subtraction is: ", a - b)
elif operation == "*":
    print("The result of multiplication is: ", a * b)
elif operation == "/":
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result of division is: ", a / b)
else:    print("Invalid operation number. Please select a valid operation.")