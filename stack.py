class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
       new_node = Node(value)
       self.top = new_node
       self.height = 1
    
    def __str__(self):
        top = self.top
        string = ""
        while top is not None:
            string += f'{top.value}\n|\n'
            top = top.next
        return string
    
    def push(self, value):
        node = Node(value)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node 
        self.height += 1
        
        return True
    
    def pop(self, ):
        if self.height == 0:
            return None
        node = self.top
        self.top = self.top.next
        node.next = None
        self.height -= 1 
        return node
                    
if __name__ == "__main__":
    s = Stack(1)
    s.push(10)
    s.push(11)
    print(s)
    s.pop()
    print(s)