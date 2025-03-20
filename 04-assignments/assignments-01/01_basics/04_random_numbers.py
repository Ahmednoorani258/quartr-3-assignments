
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def random_numbers(n: int, min_value: int, max_value: int) -> list:
    
    return [print(random.randint(min_value, max_value)) for i in range(n)]
def main():
    random_numbers(N_NUMBERS, MIN_VALUE, MAX_VALUE)
    pass

if __name__ == '__main__':
    main()