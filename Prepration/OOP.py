class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None  
    
    def add_Node(self, data):
        newNode = Node(data)
        if not self.head:  
            self.head = newNode
        else:
            temp = self.head
            while temp.next:  
                temp = temp.next
            temp.next = newNode  
    
    def print_Node(self):
        if not self.head: 
            print("List is Empty")
            return
        
        temp = self.head
        while temp:  
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("NULL")


list1 = LL()
list1.add_Node(1)
list1.add_Node(2)
list1.add_Node(3)
list1.add_Node(4)
list1.add_Node(5)
list1.add_Node(6)

list1.print_Node()
