def feet_to_inches(feet):
    return feet * 12

def main():
    user_input = float(input("Enter the number of feet: "))
    inches = feet_to_inches(user_input)
    print("There are", inches, "inches in", user_input, "feet")
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()