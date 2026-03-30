def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

num1 = 10
num2 = 0

result = divide_numbers(num1, num2)
print("Result:", result)