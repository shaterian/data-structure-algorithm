from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
        
        
        
class Tree():
    def __init__(self, val):
        self.root = Node(val)

    def insert(val):
        pass
    
# dfs time complexity o(n) spce o(n)
    def dfs_iterative(self,):
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                

    def dfs_recursive(self, root):
        if root == None:
            return []
        print(root)
        left = self.dfs_recursive(root.left) # [b d e]
        right = self.dfs_recursive(root.right) # [c f]
        
        return [root] + left + right 
        
    def bfs(self, ):
        que = deque([self.root])
        node_list = []
        while que:
            current = que.popleft()
            if current is not None:
                node_list.append(current)
            if current.left is not None:
                que.append(current.left)
            if current.right is not None:
                que.append(current.right)
        
        return node_list
        
    def contains_bfs(self, target):
        if self.root is None:
            return False
        
        q = deque([self.root])
        while q:
            current = q.popleft()
            if current.val == target:
                return True
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
        
    def contains_dfs(self, target):
        return self._contains_dfs(self.root, target)
    
    
    def _contains_dfs(self, root, target):
        if root == None:
            return False
        
        if root.val == target:
            return True
        return self._contains_dfs(root.left, target) or self._contains_dfs(root.right, target)
        
    def tree_sum(self, ):    
        return self._tree_sum(self.root)
    
    def _tree_sum(self, root):
        if root == None:
            return 0
        
        return root.val + self._tree_sum(root.left) + self._tree_sum(root.right)
    
    def max_sum_path(self):
        return self._max_sum_path(self.root)
    
    def _max_sum_path(self, root):
        if root is None:
            return -float("inf")
        if root.left is None and root.right is None:
            return root.val 
        return max(self._max_sum_path(root.left), self._max_sum_path(root.right)) + root.val
        
        

a = Node(1)
b = Node(1)
c = Node(1)
a.left = b
a.right = c 
c.left = Node(1)
b.left = Node(1)
tree = Tree(0)
tree.root = a 

bfs_list = tree.bfs()
for node in bfs_list:
    print(node.val)
print(tree.contains_bfs("a"))
print(tree.contains_dfs("a"))
print(tree.contains_dfs("f"))
print(tree.tree_sum())
print(tree.max_sum_path())

