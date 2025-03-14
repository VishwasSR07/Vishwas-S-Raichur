# 10. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operator")
