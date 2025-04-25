# 16. Function Decorators
# Assignment:
# # Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_func_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
        
    return wrapper

@log_func_call
def say_hello(name):
    print(f"Hello, {name}!")
    
# Test the decorated function
say_hello("Alice")