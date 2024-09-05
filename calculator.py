import art


def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

restart_calculator = True
while restart_calculator:
    print(art.logo)
    continue_calculations = True
    first_number = float(input("What's the first number?: "))
    while continue_calculations:
        print("+\n-\n*\n/")
        selected_key_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operations[selected_key_operation](first_number,second_number)
        print(f"{first_number} {selected_key_operation} {second_number} = {result}")
        next_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if next_operation == 'y':
            first_number = result
        if next_operation == 'n':
            continue_calculations = False
