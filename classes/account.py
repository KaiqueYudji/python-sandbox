class Account:
    name = "";
    account_number = 0;
    balance = 0;
    status = True;


    def __init__(self, name, account_number):
        self.name = name;
        self.account_number = account_number;

        return; 
 

    
    def get_name(self):
        print(self.name);

        return;



    def deposit(self, deposit_value):
        self.balance += deposit_value; 
        print(self.name + " deposited: R$" + str(deposit_value));    

        return;



    def withdraw(self, withdraw_value):

        if(self.status and self.balance > withdraw_value):
            self.balance -= withdraw_value;
            print("Withdraw of " + str(withdraw_value) + " concluded!");
        else:
            print("You can't withdraw an amount greater than " + str(self.balance));

        return;   




    def show_balance(self):
        print("Your current balance is: R$" + str(self.balance));

        return;



    def validate_status(self):
        return self.status;    

        
