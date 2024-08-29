class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Queue:
    def __init__(self, value) -> None:
        node = Node(value)
        self.length = 1
        self.first = node 
        self.last = node 
    
    def __str__(self):
        top = self.first
        string = ""
        while top is not None:
            string += f'{top.value}->'
            top = top.next
        return string
    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length+=1
        
        return True 
        
        
    def dequeue(self,):
        if self.length == 0:
            return None
        node = self.first 
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node.next = None
        self.length -= 1 
        
        return node
    
if __name__ == "__main__":
    q = Queue(3)
    print(q)
    