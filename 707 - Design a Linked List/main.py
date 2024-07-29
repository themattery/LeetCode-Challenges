class MyLinkedList:

def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
def get(self, index: int, get_node=False) -> int:
    if index < 0 or index >= self.length:
        return -1
    temp = self.head
    for _ in range(index):
        temp = temp.next
    if get_node:
        return temp
    else:
        return temp.value
    

def addAtHead(self, val: int) -> None:
    new_node = Node(val)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self.length += 1

def addAtTail(self, val: int) -> None:
    new_node = Node(val)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1

def addAtIndex(self, index: int, val: int) -> None:
    new_node = Node(val)
    if index < 0 or index >= self.length:
        return None
    elif index == 0:
        self.addAtHead(val)
    elif index == self.length:
        self.addAtTail(val)
    else:
        temp = self.get(index-1, get_node=True)
        new_node.next = temp.next
        temp.next = new_node
    self.length += 1

def deleteAtIndex(self, index: int) -> None:
    prev = self.get(index - 1, get_node=True)
    temp = prev.next
    prev.next = temp.next
    temp.next = None

class Node:
def __init__(self, value):
    self.value = value
    self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)