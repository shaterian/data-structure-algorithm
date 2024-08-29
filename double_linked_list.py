class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self) -> str:
        return f'{self.value}'
        
class DoubleyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self) -> str:
        string = ""
        current = self.head
        while current != None:
            string = string + f'{current.value}->'
            current = current.next
        return string
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
        self.length -= 1    
        return node
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1 
        return True
    
    def pop_first(self,):
        node = self.head
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        self.length -= 1     
        return node
    
    def get(self,idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx <= self.length - idx:
            temp = self.head
            for _ in range(idx):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - idx):
                temp = temp.prev
        
        return temp
    
    def set_value(self, idx, value):
        node = self.get(idx)
        if node:
            node.value = value
            return True
        return None
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        node = Node(value)
        before = self.get(index-1)
        
        node.prev = before
        node.next = before.next
        before.next.prev = node
        before.next = node
        
        self.length += 1       
        return True
        
    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            return self.pop_first()
        if idx == self.length -1:
            return self.pop() 
        current = self.head
        current = self.get(idx)
        
        current.prev.next = current.next
        current.next.prev = current.prev
        
        current.prev = None
        current.next = None
        
        self.length -= 1
        return current
        
        
        
    
if __name__ == "__main__":
    
    dll = DoubleyLinkedList(1)
    dll.append(2)
    print(dll)
    print(dll.get(1))
    dll.insert(1,3)
    print(dll)