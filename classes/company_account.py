from classes.account import Account;

""" With this code(class Company_account(Account)) --> I'm inheriting all properties from class Account to this class """
class Company_account(Account):

    def __init__(self, name, account_number):
        super().__init__(name, account_number)

        return;


    def get_loan(self, loan_value):
        if(self.status):
            self.balance += loan_value;
            print("Loan of " + str(loan_value) + "concluded!");
        else:
            print("You can't get a loan because your account status is false.");

        return;    
