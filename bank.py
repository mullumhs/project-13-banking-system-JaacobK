""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account

class Bank:
    def __init__(self):
        self._accounts = []

    # check if account exists and returns it, otherwise returns None
    def account_exist(self, acc_num):
        for account in self._accounts:
            if account.get_acc_num() == acc_num:
                print("yay")
                return account
            else:
                return None

    # usses the account exist function to add an account if it doesn't allready exists and dosn't if it allready exists
    def add_account(self, name, acc_num):
        if self.account_exist(acc_num) is not None:
            #raise ValueError("Account already exists")
            print("bad")
        else:
            new_account = Account(name, acc_num)
            self._accounts.append(new_account)

    # usses the account exist function to remove an account if it exists otherwise shows it can not be found
    def remove_account(self, acc_num):
        account = self.account_exist(acc_num)
        if account:
            self._accounts.remove(account)
        else:
            raise ValueError("Account not found")
        
    #
    def deposit(self, acc_num, amount):
        account = self.account_exist(acc_num)
        if account:
            account = self.deposit(amount)
        else:
            raise ValueError("Account not found")
    
    # 
    def withdraw(self, acc_num, amount):
        account = self.account_exist(acc_num)
        if account:
            account = self.withdraw(amount)
        else:
            raise ValueError("Account not found")
        
    def transfer(self, source_acc, dest_acc, amount):
        source_account = self.account_exist(source_acc)
        destination_account = self.account_exist(source_acc)
        if source_account and destination_account:
            source_account = self.withdraw(amount)
            destination_account = self.deposit(amount)
        else:
            raise ValueError("Account not found")

    def display(self):
        for account in self._accounts:
           print(account) 
        

me_bank = Bank()

me_bank.add_account("joe", 123)
me_bank.add_account("joe", 123)
me_bank.add_account("appleman", 1223)
me_bank.display()
me_bank.deposit(123, 100)
#me_bank.remove_account(1223)