


def main():
    for i in range(10, 0, -1):  # Starts at 10, ends at 1, decrementing by 1
        print(i, end="... ")  # Prints the countdown
    print("Liftoff!")  # Prints Liftoff! after the countdown

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()