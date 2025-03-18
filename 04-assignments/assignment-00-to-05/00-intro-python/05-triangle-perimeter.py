def main():

    side1: float = float(input("\nWhat is the length of side 1? "))
    side2: float = float(input("\nWhat is the length of side 2? "))
    side3: float = float(input("\nWhat is the length of side 3? "))

    print("\n\nThe perimeter of the triangle is " + str(side1 + side2 + side3))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()