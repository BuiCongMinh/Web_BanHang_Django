def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 2)
except ValueError as ve:
    print(f"Error: {ve}")
else:
    print(f"Result: {result}")