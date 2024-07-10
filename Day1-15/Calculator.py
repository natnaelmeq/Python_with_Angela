#Calculator
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2


operations = {

    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1= float(input("what's the first number?: "))

for symbole in operations:
    print(symbole)



# operation_symbol=input("Pick an operation from the line above: ")
# num2= int(input("what's the second number?: "))
# calculation_function=operations[operation_symbol]
# first_answer= calculation_function(num1,num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# operation_symbol=input("Pick another operation: ")
# num3= int(input("what's is next  number?: "))
# calculation_function=operations[operation_symbol]
# second_answer= calculation_function(first_answer,num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# response=input(f"type 'Y' to continue calculating with {second_answer}, or type 'n' to exit: " )
# if response=="y":
#     operation_symbol=input("Pick another operation: ")
#     num4= int(input("what's is next  number?: "))
#     calculation_function=operations[operation_symbol]
#     thired_answer= calculation_function(second_answer,num4)
#     print(f"{second_answer} {operation_symbol} {num4} = {thired_answer}")
# else:
#     print("see you soon")



should_continue= True
while should_continue:
    operation_symbol=input("Pick another operation: ")
    num2= float(input("what's is next  number?: "))
    calculation_function=operations[operation_symbol]
    answer= calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"type 'Y' to continue calculating with {answer}, or type 'n' to exit: " )=="y":
        num1=answer
    else:
        should_continue= False
