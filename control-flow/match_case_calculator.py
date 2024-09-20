number1= int(input("Enter the first number:"))
number2= int(input("Enter the second number:"))
operation= input("Choose the operation (+, -, *, /):")
result = 0

match operation:
    case "+":
        result = number1 + number2
        print("The result is ",result)
    case "-":
        result = number1 - number2
        print("The result is ",result)
    case "*":
        result = number1 * number2
        print("The result is ",result)
    case "/":
        if number2 == 0:
            print("Cannot divide by zero")
            exit()
        else:
            result = number1 / number2
        print("The result is ",result)
    case _:
        print("Invalid operation")