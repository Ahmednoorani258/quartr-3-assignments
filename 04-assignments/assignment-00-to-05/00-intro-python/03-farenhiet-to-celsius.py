def ferenhiet_to_celsius(farenhiet):
    degrees_celsius = (farenhiet - 32) * 5.0/9.0
    print(farenhiet, "degrees farenhiet is", degrees_celsius, "degrees celsius")
    


def main():
    user_input = input("Enter a temperature in farenhiet: ")
    ferenhiet_to_celsius(float(user_input))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()