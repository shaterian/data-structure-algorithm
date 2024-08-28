class LinedList():
    def __init__(self, val):

        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_ll(self,):
        print(self.head)
        

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False
        if idx == 0:
            return self.prepend(value)
        if idx ==  self.length - 1:
            return self.append(value)
        new_node = Node(value)
        prev = self.lookup_id(idx - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def pop(self, ):
        if self.head is None:
            self.length = 0
            return None
        if self.length == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return tmp
        current_node = self.head
        for _ in range(self.length - 2):
            current_node = current_node.next
        tmp = self.tail
        self.tail = current_node
        self.tail.next = None
        self.length -= 1 
        return tmp

    def pop_first(self, ):
        if self.length == 0:
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return tmp

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            return self.pop_first()
        if idx == self.length - 1:
            return self.pop()
        prev_node = self.lookup_id(idx-1)
        tmp = prev_node.next
        prev_node.next = tmp.next
        tmp.next = None
        self.length -= 1
        return tmp

    def lookup_id(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        current_node = self.head
        for _ in range(idx):
            current_node = current_node.next
        return current_node

    def lookup_val(self, value):
        pass
    
    def set_value(self, idx, value):
        node = self.lookup_id(idx)
        if node:
            node.value = value
            return True
        return False
    
    def reverse(self,):
        if self.length == 1:
            return False
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        before = None
        current = self.head
        next_node = current.next
        for i in range(self.length ):
            if i == self.length - 1:
                current.next = before 
            else:
                current.next = before 
                before = current
                current = next_node
                next_node = current.next        
                
class Node():
    def __init__(self, val, next=None):

        self.value = val,
        self.next = next
    def __str__(self) -> str:
        return f"Node({self.value},{self.next})"

if __name__ == "__main__":
    ll = LinedList(4)
    ll.append(1)
    ll.print_ll()
    # print(ll.pop_first())
    # # ll.print_ll()
    # print(ll.pop_first())
    # # ll.print_ll()
    # print(ll.pop_first())
    # print(ll)
    # ll.print_ll()
    ll.reverse()
    ll.print_ll()
    
    
    