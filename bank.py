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

    def add_account

    def account_exist(self, acc_num):
        for account in self._accounts:
            if account.get_acc_num() == acc_num:
                return True
            else:
                return False