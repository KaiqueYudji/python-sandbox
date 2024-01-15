from classes.people_account import People_account;
from classes.company_account import Company_account;
from classes.kid_account import Kid_account;


account_teste = People_account("601343360","Kaique",554321); 
account_teste.get_name();
account_teste.deposit(3500);
account_teste.withdraw(1000);
account_teste.show_balance();
account_teste.show_document();

print("------------------------------------------------------------------------------------------------------------");

sga_account = Company_account("SGA Soluções Globais em Automação", 776352);
sga_account.get_name();
sga_account.deposit(2000);
sga_account.withdraw(1000);
sga_account.show_balance();

print("------------------------------------------------------------------------------------------------------------");

kid_account = Kid_account("Bruna",11111);
kid_account.get_name();
kid_account.deposit(5000);
kid_account.withdraw(1000);
kid_account.show_balance();

