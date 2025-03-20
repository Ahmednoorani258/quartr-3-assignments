def double_list(lst:list):
    return [x*2 for x in lst]


def main():
    print(double_list([1, 2, 3]))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()