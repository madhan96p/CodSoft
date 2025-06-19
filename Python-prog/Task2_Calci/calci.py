# CodSoft - Task 1: Simple Calculator
# Created by Pragadeesh 💡
# GitHub: github.com/madhan96p | Portfolio: pragadeeshfolio.netlify.app

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Division by zero!"
    return x / y

# Operation choices
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide)
}

# Display options
print("🔢 Simple Python Calculator")
print("---------------------------")
for key, (name, _) in operations.items():
    print(f"{key}. {name}")

# User Input
choice = input("Select an operation (1/2/3/4): ")
if choice in operations:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"✅ Result of {operation_name} = {result}")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers.")
else:
    print("❌ Invalid operation choice.")
