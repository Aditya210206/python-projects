def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":division
            }

game_over=False
while not game_over:
    num1=float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbols=input("What symbol do u choose?:")
    if operation_symbols not in operations:
        print("Please enter a valid symbol")
        continue
    num2=float(input("What is the second number?: "))
    result=operations[operation_symbols](num1,num2)
    want_to_continue=input("Do u want to continue the operation?('y' for yes and 'n' for no): ")
    if want_to_continue=='y':
        
        for symbol in operations:
            print(symbol)
        operation_symbols=input("What symbol do u choose?:")
        num3=float(input("Enter the number: "))
        final_result=operations[operation_symbols](result,num3)
        print(final_result)

    elif want_to_continue=='n':
        game_over=True
        print(result)
    else:
        print("Please enter a valid input")