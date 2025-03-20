def leap_year(year):
    if year % 4 == 0:  
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else: 
            print("That's a leap year!")
    else: 
        print("That's not a leap year.")


def main():
    year = int(input("Enter a year: "))
    leap_year(year)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()