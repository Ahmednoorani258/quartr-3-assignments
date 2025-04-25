# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class bank:
    bank_name = "Default Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
        
    @classmethod
    def display_bank_name(cls):
        print(f"The bank name is: {cls.bank_name}")
    
# Create instances of the Bank class
bank1 = bank()
bank2 = bank()

# Display the bank name using the class method
bank.display_bank_name()

# Change the bank name using the class method
bank.change_bank_name("New Bank")

# Display the bank name again to see the change
bank.display_bank_name()
