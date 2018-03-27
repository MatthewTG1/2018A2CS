#MatthewS3C5
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next (self):
        return self.next_node 
    def set_next (self, n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data = d
class LinkedList (object):
    def __init__(self, t = None, r = None):
        self.root = r
        self.tail = t
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.root = new_node
            self.tail = new_node
        self.size += 1
    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    def remove (self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def printList (self):
        List = []
        this_node = self.root
        while this_node:
            List.append(this_node.get_data())
            this_node = this_node.get_next()
        print (List) 
         
myList = LinkedList() 
myList.add(5)
myList.add(10)
myList.add(15)
myList.add(6)
myList.add(8)
myList.printList()
myList.remove(10)
myList.printList()
print(myList.find(15))
print(myList.remove(8))
