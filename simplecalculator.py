print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input()

if operation == '1':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is " + str(num1 + num2))
elif operation == '2':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The difference is " + str(num1 - num2))
elif operation == '3':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The product is " + str(num1 * num2))
elif operation == '4':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 != 0:
        print("The quotient is " + str(num1 / num2))
    else:
        print("Error! Division by zero.")
else:
    print("Invalid entry")
