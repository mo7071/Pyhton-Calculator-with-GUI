# Mini Calculator

# A simple command line calculator bulitd using Python.

# Features:
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Modulus

# Techonologies: Python

def mini_calculator ():

    num1 = int (input("Enter first num: "))

    operator = input ("Use operator  +  -  *  /  % : ")

    num2 = int (input ("Enetr second num: "))

    if operator == "+":
        return   num1 + num2

    elif operator == "-":
        return  num1 - num2

    elif operator == "*":
        return  num1 * num2

    elif operator == "/":
        return  num1 / num2

    elif operator == "%":
        return  num1 % num2

    else:
        return "Invalid choice" 
    
result = mini_calculator()
print("Result:",result) 














