def double_it (num):
    curr_val = num
    while curr_val < 100:
        curr_val *= 2
        print(curr_val)
    return curr_val
def main():
    user_input = int(input("Enter a number: "))
    double_it(user_input)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()