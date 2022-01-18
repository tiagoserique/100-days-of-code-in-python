
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    operations_finished = False

    while not( operations_finished ):
        operation_symbol = input("\nPick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        new_operation = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if ( new_operation == 'n' ):
            operations_finished = True
            calculator()
        else:
            num1 = answer
    

calculator()