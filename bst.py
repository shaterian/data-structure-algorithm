class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self,):
        self.root = None
        self.height = 0 
    
    def __str__(self):
        return str(self.root.value)
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        current = self.root
        while (True):
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None: 
                    current.left = new_node
                    return True
                current = current.left 
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
    
    def contain(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        return False    

if __name__ == "__main__":
    tree = BST()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    print(tree)
    print(tree.root.left.value)
    print(tree.root.right)
    print(tree.contain(1    ))
    