""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest = 0):
        self.__balance__ = balance
        self.__interest__ = interest

    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.__balance__ = balance

    def get_balance(self): 
        """Gets the balance for the for the account"""
        return self.__balance__

    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.__interest__ = interest

    def get_interest(self): 
        """Gets the interest gained for the the account"""
        return self.__interest__   
