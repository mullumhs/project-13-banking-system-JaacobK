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
                return account
            else:
                return None

    # usses the account exist function to add an account if it doesn't allready exists and dosn't if it allready exists
    def add_account(self, name, acc_num):
        if self.account_exist(acc_num) is not None:
            raise ValueError("Account allready exists")
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
    def deposit(self):
        pass
    
    # 
    def withdraw(self):
        pass
        
    def transfer():
        pass
    