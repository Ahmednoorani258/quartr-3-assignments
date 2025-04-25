# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn         # Private variable

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
    
# Create an instance of Employee
employee = Employee("John Doe", 50000, "123-45-6789")

# Access public variable
print(employee.name)  # Output: John Doe

# Access protected variable
print(employee._salary)  # Output: 50000

# Access private variable
# print(employee.__ssn)  # Output: 123-45-6789
# This will raise an AttributeError
# print(employee.__ssn)  # Uncommenting this line will raise an AttributeError
# Accessing private variable using name mangling
print(employee._Employee__ssn)  # Output: 123-45-6789

employee.display()