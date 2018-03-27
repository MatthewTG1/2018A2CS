
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, top=None):
        self.top = top
        
    def get_top(self):
        return self.top

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        return
         

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        node = self.top.data
        self.top = self.top.next
        return node
                  
        

    def printList(self):
        List = []
        new_node = self.top
        while new_node:
            List.append(new_node.data)
            new_node = new_node.next
        print (List)



if __name__ == '__main__':

    stack = LinkedList()       

    
    stack.push(40)
    stack.push(50)
    stack.printList()
    stack.pop()
    stack.printList()
    stack.pop()
    stack.printList()

        
