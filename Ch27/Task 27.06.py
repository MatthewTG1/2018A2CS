import datetime
class LibraryItem:
	def __init__(self, t, a, i):
		self.__Title = t
		self.__Author__Artist = a
		self.__ItemID = i
		self.__OnLoan = False
		self.__DueDate = datetime.date.today()

	def GetTitle(self):
		return(self.__Title)

	def GetAuthor__Artist(self):
		return(self.__Author__Artist)

	def GetItemID(self):
		return(self.__ItemID)

	def GetOnLoan(self):
		return(self.__OnLoan)

	def GetDueDate(self):
		return(self.__DueDate)

	def Borrowing(self, BorrowerID):
		self.__OnLoan = True
		self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
		self.BorrowerID = BorrowerID

	def Returning(self):
		self.__OnLoan = False

	def PrintDetails(self):
		print(self.__Title, '; ', self.__Author__Artist,'; ', end='')
		print(self.__ItemID,'; ', self.__OnLoan,'; ', self.__DueDate)

class Book(LibraryItem):
	def __init__(self, t, a, i):
		LibraryItem.__init__(self, t, a, i)
		self.__IsRequested = False
		self.__RequestedBy = 0
	def GetIsRequested(self):
		return(self.__IsRequested)

	def SetIsRequested(self, BorrowerID):
		self.__IsRequested = True
		self.__RequestedBy = BorrowerID

	def RetRequestedBy(self):
		self.__IsRequested = False

	def GetRequestedBy(self):
		return(self.__RequestedBy)

	def PrintDetails(self):
		LibraryItem.PrintDetails(self)
		print(" Requ: "+str(self.__IsRequested)+";\n RequBy: "+str(self.__RequestedBy)+";\n")

class CD(LibraryItem):
	def __init__(self, t, a, i):
		LibraryItem.__init__(self, t, a, i)
		self.__Genre = ""

	def GetGenre(self):
		return(self.__Genre)

	def SetGenre(self, g):
		self.__Genre = g

class Borrower:
	def __init__(self, BorrowerName, EmailAddress, BorrowerID):
		self.__BorrowerName = BorrowerName
		self.__EmailAddress = EmailAddress
		self.__BorrowerID = BorrowerID
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
		print(self.__BorrowerName, "; ", self.__EmailAddress, "; ", self.__BorrowerID)



a = Book("Steve Jobs", "Walter Isaacson", 1234)
a.PrintDetails()
b = Borrower("Matt", "Matt@163.com", 111111)
b.PrintDetails()

def Borrow(CurrBook, CurrBorr):
	CurrBook.Borrowing(CurrBorr.GetBorrowerID())
	CurrBorr.UpdateItemsOnLoan()
	CurrBook.SetIsRequested(CurrBorr.GetBorrowerID())

Borrow(a,b)
a.PrintDetails()
b.PrintDetails()