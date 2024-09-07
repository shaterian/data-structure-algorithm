from collections import deque
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

    def find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
            
    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            print("found node")
            if current_node.left is None and current_node.right is None:
                print("found node1")
                return None
            elif current_node.right is None:
                print("found node2")
                current_node =  current_node.left
            elif current_node.left is None:
                print("found node3")
                current_node =  current_node.right
            else:
                print("node has childere")
                subtree_min = self.find_min(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        return current_node
    
    def _delete_node(self, value):
        self.__delete_node(self.root, value)
    
    def bfs(self,):
        queue = []
        result = []
        current_node = self.root
        queue.append(current_node)
        while(len(queue) > 0):
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return result
    
    def dfs_pre_order(self, ):
        result = []
        def travers(node):
            result.append(node.value)
            if node.left:
                travers(node.left)
            if node.right:
                travers(node.right)
        travers(self.root)
        
        return result 
    
    def dfs_post_order(self, ):
        result = []
        def travers(node):
            if node.left:
                travers(node.left)
            if node.right:
                travers(node.right)
            result.append(node.value)
            
        travers(self.root)
        
        return result 
    
    
    def dfs_in_order(self, ):
        result = []
        def travers(node):
            if node.left:
                travers(node.left)
            result.append(node.value)
            if node.right:
                travers(node.right)
            
        travers(self.root)
        
        return result 
    def bfs_level(self,):
        if self.root == None:
            return []
        
        q = deque([self.root])
        level_lists = []
        while(q):
            level_size = len(q)
            level_list = []
            for _ in range(level_size):
                node = q.popleft()
                level_list.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_lists.append(level_list)
        return level_lists
    
    def max_height(self,):
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
        
        return traverse(self.root) - 1
    
                
        
        
        
if __name__ == "__main__":
    tree = BST()
    tree.insert(47)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(4.5)
    tree.insert(4.6)
    tree.insert(7)
    
    # print(tree.bfs())
    # print(tree.dfs_in_order())
    # print(tree.dfs_pre_order())
    # print(tree.dfs_post_order())
    print(tree.bfs_level())
    print(tree.max_height())