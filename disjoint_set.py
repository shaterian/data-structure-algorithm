# Quick Find
# Store the root node for each vertix instead of the parent 
# Find becom o(1)
# Drawback should search all nodes in the union you should find all the element with the root 
# you are connecting and change their root O(n)
class UnionQuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
                    
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
# Quick Union 
# Save the parent of each vertext in the vertex index 
# to get the root of a vertext you should travers through parent to get the vertex
# The find becom O(n)
# The Union become easy because you just set the parent of the root of the new connected 

class UnionQuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]
                    
    def find(self, node):        
        while node != self.root[node]:
            node = self.root[node]
        return node
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Union by Rank 
# During union choose the root with higher rank to be the joint root to prevent increaing height 
# This way tree becomes balanced and the find becoms o(log(n))

class UnionQuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
                    
    def find(self, node):        
        while node != self.root[node]:
            node = self.root[node]
        return node
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
    
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1 
        
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# path compression optimization
class UnionQuickFindOptimized:
    def __init__(self, size):
        self.root = [i for i in range(size)]
                    
    def find(self, node):        
        if node == self.root[node]:
            return node     
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
                self.root[root_y] = root_x
            
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# optimized 
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
	# Some ranks may become obsolete so they are not updated
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)



# Test Case
uf = UnionQuickFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
