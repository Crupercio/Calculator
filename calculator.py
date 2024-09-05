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
operations_symbol = ["+","-","*","/"]

restart_calculator = True
while restart_calculator:
    print(art.logo)
    continue_calculations = True
    first_number = float(input("What's the first number?: "))
    while continue_calculations:
        print("+\n-\n*\n/")
        selected_key_operation = input("Pick an operation: ")
        if selected_key_operation in operations_symbol:
            second_number = float(input("What's the next number?: "))
            result = operations[selected_key_operation](first_number,second_number)
            print(f"{first_number} {selected_key_operation} {second_number} = {result}")
            next_operation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'x' to exit : ")
            if next_operation == 'y':
                first_number = result
            elif next_operation == 'n':
                continue_calculations = False
            else:
                restart_calculator = False
                continue_calculations = False

        else:
            print("Wrong operator")

