class node:
    def __init__(self,value,pointer):
        self.value = value
        self.pointer = pointer

def CreateNewList():
    global HeadNode
    HeadNode = None
def DeleteList():
    global HeadNode
    HeadNode = None
def InsertNode(pos, N):
    global HeadNode
    curr = HeadNode
    nodex = node(N, None)
    PosCounter = 1
    if pos == 0:
        HeadNode = nodex
        nodex.pointer = curr
    else:
        while (pos > PosCounter):
            curr = curr.pointer
            PosCounter += 1
        nodex.pointer = curr.pointer
        curr.pointer = nodex
def DeleteNode(N):
    global HeadNode
    prev = None
    curr = HeadNode
    if curr.value == N:
        HeadNode = curr.pointer
    else:
        while (curr.pointer != None) and (curr.value != N):
            prev = curr
            curr = curr.pointer
        prev.pointer = curr.pointer

def PrintList():
    global HeadNode
    curr = HeadNode
    if curr != None:
        while curr != None:
            print("[",curr.value,"]", end = "")
            curr = curr.pointer
    else:
        print("Empty List")

CreateNewList()
InsertNode(0,25)
InsertNode(1,30)
InsertNode(2,35)
InsertNode(1,28)
DeleteNode(30)
PrintList()




