class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    ### Partition function ###
    def partition_list(self, x):
        if self.head is None:
            return None
            
        dummy1 = dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        
        current_node = self.head
        
        while current_node is not None:
            if current_node.value < x:
                prev1.next = current_node
                prev1 = current_node
            else:
                prev2.next = current_node
                prev2 = current_node
            current_node = current_node.next
        prev1.next = prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next
            