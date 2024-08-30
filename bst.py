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
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
        
    def __r_insert(self, current_node, value):
        if current_node.left is None:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value < current_node.left:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.right:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.right is None and current_node.let is None:
                return None
            elif current_node.left:              
                current_node = current_node.left
            else:
                while current_node.left:
                    current_node = current_node.left
        return current_node 

if __name__ == "__main__":
    tree = BST()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    print(tree)
    print(tree.root.left.value)
    print(tree.root.right)
    print(tree.contain(1))
    print(tree.r_contains(1))

    