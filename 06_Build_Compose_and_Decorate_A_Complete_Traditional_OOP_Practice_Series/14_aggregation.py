 
# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def get_employee_name(self):
        return self.employee.get_name()
    
# Example usage
employee = Employee("Alice")
department = Department("HR", employee)

print(department.get_employee_name())  
    