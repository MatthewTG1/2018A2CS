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

        def PrintDetails(self):
                LibraryItem.PrintDetails(self)
                print(self.__Genre)

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


def DisplayMenu():
        print("1 - Add a new borrower")
        print("2 - Add a new book")
        print("3 - Add a new CD")
        print("4 - Borrow book")
        print("5 - Return book")
        print("6 - Borrow CD")
        print("7 - Return CD")
        print("8 - Request book")
        print("9 - Print all details")
        print("99 - Exit program")
        print()
        print("Enter your menu choice: ")

def main():
        Finish = False
        NextBorrowerID = 1
        NextBookID = 1
        NextCD_ID = 1
        
        while Finish == False:
                DisplayMenu()
                MenuChoice = int(input())
                if MenuChoice == 1:
                        Name = input("Name: ")
                        Email = input("Email: ")
                        BorrowerID = input("BorrowerID: ")
                        NextBorrowerID = NextBorrowerID + 1
                        Borrower1 = Borrower(Name, Email, BorrowerID)
                elif MenuChoice == 2:
                        Title = input("Title: ")
                        Author = input("Author: ")
                        ItemID = NextBookID
                        NextBookID += 1
                        NewBook = Book(Title, Author, ItemID)
                elif MenuChoice == 3:
                        Title = input("Title: ")
                        Author = input("Author: ")
                        ItemID = NextCD_ID
                        NextCD_ID += 1
                        NewCD = CD(Title, Author, ItemID)
                elif MenuChoice == 4:
                        BorrowerID = input("Borrower ID: ")
                        ItemID = input("Book ID: ")
                        Book.Borrowing(ItemID, Borrower1)
                elif MenuChoice == 5:
                        BorrowerID = input("Borrower ID: ")
                        ItemID = input("Book ID: ")
                        Book.Returning(ItemID, Borrower1)
                elif MenuChoice == 6:
                        BorrowerID = input("Borrower ID: ")
                        ItemID = input("CD ID: ")
                        CD.Borrowing(ItemID, Borrower1)
                elif MenuChoice == 7: 
                        BorrowerID = input("Borrower ID: ")
                        ItemID = input("CD ID: ")
                        CD.Returning(ItemID, Borrower1)
                elif MenuChoice == 8:
                        BorrowerID = input("Borrower ID: ")
                        ItemID = ("Book ID: ")
                        Book.SetRequestedBy(ItemID, Borrower1)
                elif MenuChoice == 9:
                        print("Borrower Details")
                        Borrower.PrintDetails()
                        print("Book Details")
                        Book.PrintDetails()
                        print("CD Details")
                        CD.PrintDetails()
                elif MenuChoice == 99:
                        Finish = True
                else:
                        print("wrong input")
        input()

main()


