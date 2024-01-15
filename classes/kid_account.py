from classes.account import Account;

class Kid_account(Account):

    def __init__(self, name, account_number):
        super().__init__(name, account_number);

        return;



    def deposit(self, deposit_value):
        self.set_balance_add_10(deposit_value);
        print(self.name + " deposit was registred with one addition of 10R$ = " + str(deposit_value + 10));

        return;



    def set_balance_add_10(self, deposit_value):
        self.balance += (deposit_value + 10);

        return;

