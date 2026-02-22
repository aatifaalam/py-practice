# Make a calculator that can be basic operations like addition, subtraction, multiplication, and divider

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Please select")
print("+ for addition.")
print("- for substraction ")
print("* for multiplication.")
print("/ for division")
calc = (input("Enter the operation you want to perform: "))


if( calc == "+"):
    print("Addition of a and b is: ", a + b)
elif( calc == "-"):
    print("Substraction of a and b is: ", a - b)
elif( calc == "*"):
    print("Multiplication of a and b is: ", a * b)
elif( calc == "/"):
    print("Division of a and b is: ", a / b)
else:
    print("Please enter a valid operation.")