class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        

    def isEmpty(self):
        if self.tail == None and self.head == None:
            return True
        else:
            return False

    def enqueue(self, num):  
        node = Node(num)  
        if self.isEmpty():  
            self.head = node  
            self.tail = node  
        else:  
            self.tail.next = node  
            self.tail = node  

    def dequeue(self):
        if self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.head
            self.head = popped.next
            

    def printList(self):
        List = []
        new_node = self.head
        while new_node:
            List.append(new_node.data)
            new_node = new_node.next
        print (List)

if __name__ == '__main__':

    queue = LinkedList()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.printList()
    queue.dequeue()
    queue.printList()
    queue.dequeue()
    queue.printList()
    
    


        
        
        
        
