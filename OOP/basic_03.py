# Encapsulation

# create getter and setter

class BalanceSheet:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return f"The balance is: {self.__balance}.00 Rs/-"

    def set_balance(self,balance):    
        self.__balance = balance


bank_of_baroda_account = BalanceSheet()
bank_of_baroda_account.set_balance(5000000)
print(bank_of_baroda_account.get_balance())