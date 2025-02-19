def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    # List of operations
    operations = [add, subtract, multiply, divide]
    numbers = [(10, 5), (20, 4), (15, 3), (9, 0)]

    # Perform each operation on each pair of numbers
    for operation in operations:
        for num1, num2 in numbers:
            result = operation(num1, num2)
            print(f"{operation.__name__}({num1}, {num2}) = {result}")   #operation.__name__ just takes the name and translates it to a string

    # List comprehension to create a list of results for addition
    addition_results = [add(num1, num2) for num1, num2 in numbers]
    print("Addition results:", addition_results)

    # Dictionary to store results of all operations
    results_dict = {operation.__name__: [operation(num1, num2) for num1, num2 in numbers] for operation in operations}
    print("Results dictionary:", results_dict)