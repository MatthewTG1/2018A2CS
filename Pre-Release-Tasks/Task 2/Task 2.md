Task 2.1 and 2.2

Toy:

Name:STRING
ID:STRING
Price:FLOAT
MinimumAge:INTEGER

Constructor()
GetName()
GetID()
GetPrice()
GetMinimumWage()
SetName()
SetID()
SetPrice()
SetMinimumWage()

ComputerGame:

Catagory:STRING
Console:STRING

Constructor()
GetCatagory()
GetConsole()
SetCatagory()
SetConsole()

Vehicle:

Type:STRING
Height:FLOAT
Length:FLOAT
Weight:FLOAT

Constructor()
GetType()
GetHeight()
GetLength()
GetWeight()
SetType()
SetHeight()
SetLength()
SetWeight()

Inheritance
Where all attributes and methods of base class are copied to subclass

Task 2.3

class Toy:
	def __init__(self):
		self.__Name = ""
		self.__ID = ""
		self.__Price = 0
		self.__MinimumAge = 0

	def GetName(self):
		return self.__Name

	def GetID(self):
		return self.__ID

	def GetPrice(self):
		return self.__Price

	def GetMinimumAge(self):
		return self.__MinimumAge 

	def SetName(self,n):
		self.__Name = n

	def SetID(self,i):
		self.__ID = i 

	def SetPrice(self,p):
		self.__Price = p

	def SetMinimumAge(self,m):
		self.__MinimumAge = m

Task 2.4

class ComputerGame:
	def __init__(self):
		Toy.__init__(self)
		self.__Category = ""
		self.__Console = ""

	def GetCategory(self):
		return self.__Category

	def GetConsole(self):
		return self.__Console 

	def SetCategory(self,c):
		self.__Category = c

	def SetConsole(self,c):
		self.__Console = c

class Vehicle:
	def __init__(self):
		Toy.__init__(self)
		self.__Type = ""
		self.__Height = 0
		self.__Length = 0
		self.__Weight = 0 

	def GetType(self):
		return self.__Type 

	def GetHeight(self):
		return self.__Height

	def GetLength(self):
		return self.__Length

	def GetWeight(self):
		return self.__Weight 

	def SetType(self,t):
		self.__Type = t

	def SetHeight(self,h):
		self.__Height = h

	def SetLength(self,l):
		self.__Length = l 

	def SetWeight(self,w):
		self.___Weight = w

Task 2.5

class Toy:
	def SetMinimumAge(self,m):
		while type(m) != int and (m>18 or m<0):
			m = input("Input minimum age: ")
		self.__MinimumAge = m

class ComputerGames:
	def SetCategory(self,c):
		while type(c) != str:
			c = input("Input category: ")
		self.__Category = c

class Vehicle:
	def SetHeight(self,h):
		while type(h) != int and type(h) != float:
			h = input("Input height: ")
		self.__Height = h

	def SetLength(self,l):
		while type(l) != int and type(l) != float:
			l = input("Input length: ")
		self.__Length = l

	def SetWeight(self,w):
		while type(w) != int and type(w) != float:
			w = input("Input weight: ")
		self.__Weight = w
Task 2.6

toyArray = []
newToy = Vehicle()
newToy.SetName("Red Sports Car")
newToy.SetID("RSC13")
newToy.SetMinimumAge(6)
newToy.SetType("Car")
newToy.SetHeight(3.3)
newToy.SetLength(12.1)
newToy.SetWeight(0.08)
toyArray.append(newToy)
2.7

class Toy:
	def PrintInfo(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)

class ComputerGame(self):
	def PrintInfo(self):
		print("Computer game:")
		toy.PrintInfo(self)
		print(" Category:",self.__Category)
		print(" Console:",self.__Console)

class Vehicle(self):
	def PrintInfo(self):
		print("Vehicle:")
		toy.PrintInfo(self)
		print(" Type:",self.__Type)
		print(" Height:",self.__Height)
		print(" Length:",self.__Length)
		print(" Weight:",self.__Weight)

def FindToy(ID):
	for i in toyArray:
		if i.GetID == ID:
			i.PrintInfo()
			break
	print("Requested toy not found")
2.8

import random 
class Toy:
	def Discount(self,d):
		self.__Price *= 1-d/100

def DiscountAll(d):
	toys = []
	for i in range(10):
		toys.append(ComputerGamme())
	for i in range(10):
		toys.append(Vehicle())
	for i in range(len(toys)):
		toys[i].setPrice(random.randint(1,200))
	for i in toys:
		i.Discount(d)

DiscountAll(10)
for i in range(len(toys)):
	i.PrintInfo()
Task 2.9 

Bubble sort is a sort method where adjacent pairs of values are compared & swapped.
Insertion sort is a sort method where values a inserted into a stack one by one.
In insertion sort elements are bubbled into the sorted section, while in bubble sort the maximums are bubbled out of the unsorted section.

Task 2.10

sortedToys = [0 for i in range(len(toys))]
sortedToys[0] = toys[0]
for i in range(1,len(toys)):
	newToy = toys[i]
	currP = currP - 1
	while sortedToy[currP].GetPrice() > newToy.GetPrice() and currP >= 0:
		sortedToy[currP+1] = sortedToy[currP]
		currP = currP -1
	sortedToy[currP+1] = newToy
for i in sortedToys:
	i.PrintInfo()



