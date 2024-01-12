class Account:
    name;
    account_number;
    balance;
    status;


    def __init__(self, name, account_number, balance, status):
        self.name = name;
        self.account_number = account_number;
        self.balance = balance;
        self.status = status;
        return;
 

    
    def get_name(self):
        print(self.name);