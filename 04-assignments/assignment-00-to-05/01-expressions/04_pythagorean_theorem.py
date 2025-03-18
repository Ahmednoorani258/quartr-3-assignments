import math

def pythagorean_theorem(AB, AC):
    return math.sqrt(AB**2 + AC**2)

def main():
    AB = float(input("Enter the length of side AB: "))
    AC = float(input("Enter the length of side AC: "))
    hypotenuse = pythagorean_theorem(AB, AC)
    print(AB ** 2)
    print(AC ** 2)
    print(math.sqrt(50))
    print("The length of the hypotenuse is:", hypotenuse)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()