from classes.account import Account;

class People_account(Account):
    document_id = "";

    def __init__(self, document_id,  name, account_number):
        super().__init__(name, account_number);
        self.document_id = document_id;

        return;



    def show_document(self):
        print(self.document_id);

        return;    
