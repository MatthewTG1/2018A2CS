class Borrower:
	def __init__(self):
		self.__BorrowerName = ""
		self.__EmailAddress = ""
		self.__BorrowerID = None
		self.__ItemsOnLoan = 0

	def __repr__(self):
		return "Name: %s; Addr: %s; ID: %s; onLoan: %d" %(self.__BorrowerName, self.__EmailAddress, self.__BorrowerID, self.__ItemsOnLoan)

	def GetBorrowerName(self):
		return self.__BorrowerName

	def GetEmailAddress(self):
		return self.__EmailAddress

	def GetBorrowerID(self):
		return self.__BorrowerID

	def GetItemsOnLoan(self):
		return self.__ItemsOnLoan

	def UpdateItemsOnLoan(self):
		self.__ItemsOnLoan += 1

	def PrintDetails(self):
		print(self.__BorrowerName, "")

a = Borrower()
a.UpdateItemsOnLoan()
print(a)


