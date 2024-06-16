""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    def __init__(self, name, acc_num, balance):
        self.set_name(name)
        self.set_acc_num(acc_num)
        self.set_balance(balance)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            raise ValueError("not a valid name")

    def get_acc_num(self):
        return self._acc_num
    
    def set_acc_num(self, acc_num):
        if isinstance(acc_num, int) and acc_num >= 0:
                self._acc_num = acc_num
        else:
            raise ValueError("Not a valid int")

    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        if isinstance(balance, float, int) and balance >= 0:
                self._acc_num = balance
        else:
            raise ValueError("Not a valid int")
        
    def deposit(self, balance, deposit_amount):
        if deposit_amount > 0:
            self._balance = balance + deposit_amount
        else:
            raise ValueError("Not a valid deposit")
        
    def withdraw(self, balance, withdraw_ammount):
        if withdraw_ammount > 0 and balance - withdraw_ammount >= 0:
            self._balance = balance - withdraw_ammount
        else:
            raise ValueError("Not a valid withdraw")
         
        
    