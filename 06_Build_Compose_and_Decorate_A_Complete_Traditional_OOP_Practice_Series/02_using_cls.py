
# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class counter:
    count = 0 # Class variable to keep track of the number of objects created
    def __init__(self):
        counter.count += 1 # Increment the count whenever a new object is created
    
    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}") # Display the count using the class variable
        
# Create instances of the Counter class
counter1 = counter()
counter2 = counter()
counter3 = counter()

# Display the count using the class method
counter.display_count()