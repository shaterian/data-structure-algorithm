class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class AVL_tree:
    def __init__(self, val):
       self.root = Node(val)
       
    def insert(self,):
        pass
        
    def right_rotate(self, ):
        
        
        
        
    def balance_score(self, node):
        def traverse(node):
            if not node:
                return 0 
            right_most = 0 
            left_most = 0  
            if node.right:
                right_most = traverse(node.right)
            if node.left:
                left_most = traverse(node.left)
            return max(right_most, left_most) + 1
        
        right_height = traverse(node.right) - 1
        left_height = traverse(node.left) - 1 
        
        return left_height - right_height
                
                
