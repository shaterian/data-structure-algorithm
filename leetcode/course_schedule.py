class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == []:
            return True 

        graph = {i: [] for i in range(numCourses)}
        for ai, bi in prerequisites:
            graph[ai].append(bi)
        
        print(graph)
        visited = set()
        for node in range(numCourses):
            if self.has_cycle(graph, node, visited):
                return False
        return True


    def has_cycle(self, graph, node, visited=None, stack=None):
        
        print(f"debug has_cycle node is {node}")
        
        if stack is None:
            stack = []
        if node in stack:
            return True
        
        stack.append(node)
        
        if  graph[node] == []:
            print("if  graph[node] == []:")
            return False 
            
        for nb in graph[node]:
            if nb in visited:
                return False
            if self.has_cycle(graph, nb, visited, stack):
                return True 
        
        visited.add(node)
        stack.pop()
        return False 
    
s = Solution()
print(s.canFinish(2, [[1,0], [0,1]]))