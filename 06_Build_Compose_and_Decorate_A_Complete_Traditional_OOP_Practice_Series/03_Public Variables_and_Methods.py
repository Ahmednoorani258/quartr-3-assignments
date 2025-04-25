# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} is starting.")

# Create an instance of the Car class
my_car = car("Toyota")  
# Access the public variable
print(my_car.brand)  # Output: Toyota
# Call the public method
my_car.start()  # Output: Toyota is starting.
        