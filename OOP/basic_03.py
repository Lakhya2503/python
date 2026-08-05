# Encapsulation

# create getter and setter

class BalanceSheet:
    def __init__(self):
        self.__balance = 0 
        # the __balance is private for other but not for our class 
        # when you wan't to access the __balance 
        # you can't directly write the .__balace beacuse 
        # when you put the __ in any variable name on first
        # then it's a private variable for other but not for our 
        # class so you will create the getter setter method for access on outsice the class

    def get_balance(self):
        return f"The balance is: {self.__balance}.00 Rs/-"

    def set_balance(self,balance):    
        self.__balance = balance


bank_of_baroda_account = BalanceSheet()
bank_of_baroda_account.set_balance(5000000)
print(bank_of_baroda_account.get_balance())