from logo import log

def add(n1, n2):
    return n1 + n2
    
def substrack (n1, n2):
    return  n1 - n2
    
def multiply (n1, n2):
    return  n1 * n2
    
def devide (n1, n2):
    return n1 / n2
    

operations = {
    "+": add,
    "-": substrack,
    "*": multiply,
    "/": devide
}

def calculation():
    print(log)
    num1 = float(input("What's the first number : "))

    should_accumulate = True
    while should_accumulate:
        for i in operations:
            print(i)
        operations_symbols = input("Pic an operatons : ")
        num2 = float(input("What's the next number : "))

        if operations_symbols not in operations:
            print("Operator not found!")
            continue

        result = operations[operations_symbols] (num1,num2)
        print(f"{num1} {operations_symbols} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()
        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            
calculation()

