class BankAccount:
    def __init__(self, i):
        self.__AccountHolderName = ""
        self.__IBAN = i

    def SetAccountHolderName(self, n):
        self.__AccountHolderName = n

    def GetAccountHolderName(self):
        return(self.__AccountHolderName)

    def GetIABN(self):
        return(self.__IABN)



