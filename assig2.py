number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print("\n--- BASIC CALCULATOR ---")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("% : Modulo")
print("** : Exponentiation")
print("// : Floor Division")
print("/ : Division")
operator = input("\nEnter the operator you want to use: ")



if operator == "+":
    answer = number1 + number2

elif operator == "-":
    answer = number1 - number2

elif operator == "*":
    answer = number1 * number2

elif operator == "%":
    if number2 == 0:
        answer = "Error: Cannot perform modulo by zero"
    else:
        answer = number1 % number2

elif operator == "**":
    answer = number1 ** number2

elif operator == "//":
    if number2 == 0:
        answer = "Error: Cannot perform floor division by zero"
    else:
        answer = number1 // number2

elif operator == "/":
    if number2 == 0:
        answer = "Error: Cannot divide by zero"
    else:
        answer = number1 / number2

else:
    answer = "Invalid operator selected!"


print("\nCalculation Result:", answer)
