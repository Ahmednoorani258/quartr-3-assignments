def get_user_numbers():
    user_numbers = []
    
    while True:
        user_input = input("Enter a number: ")
        if user_input == "done" or user_input == "Done" or user_input == "":
            break
        user_numbers.append(int(user_input))
    
    return user_numbers


def count_numbers(numbers:list):
    num_dict = {}
    for num in numbers:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return num_dict

def print_numbers(num_dict:dict):
    for key, value in num_dict.items():
        print(f"{key} appears {value} times")
    

def main():
    user_numbers = get_user_numbers()
    num_dict = count_numbers(user_numbers)
    print_numbers(num_dict)

if __name__ == "__main__":
    main()