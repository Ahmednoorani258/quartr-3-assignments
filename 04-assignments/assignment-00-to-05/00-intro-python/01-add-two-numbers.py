def main():
    print("Add 2 numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("Sum of", num1, "and", num2, "is", sum)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()