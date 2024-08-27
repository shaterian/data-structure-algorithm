class LinedList():
    def __init__(self, val):
        
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_ll(self,):
        current_node = self.head
        if current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        
    def append(self, value):
        pass
    def prepend(self, value):
        pass
    def insert(self, value):
        pass
    def pop(self, value):
        pass
    def pop_first(self, value):
        pass
    def remove(self, value):
        pass
    def lookup_id(self, id):
        pass
    def lookup_val(self, value):
        pass
    
class Node():
    def __init__(self, val, next=None):
        
        self.value = val,
        self.next = next
        
if __name__ == "__main__":
    ll = LinedList(4)
    ll.print_ll()