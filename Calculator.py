def main():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "^":
        print(num1 ** num2)
    else:
        print("INVALID INPUT")

    restart = (input("Do you want to restart: "))

    if restart == "yes":
        main()
    else:
        exit()

main()