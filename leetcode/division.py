class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        
        """
        graph = {
        
        "v1": {"v2": 1, "v3": 3}
        
        }
        
        """
        graph = self.buildGraph(equations, values)
        print(graph)
        
        result = []
    
        for q in queries:
            visited = set()
            if q[0] not in graph or q[1] not in graph:
                result.append(-1)
            else:
                result.append(self.find_path(graph, q[0], q[1], visited))
            
        return result 
        
    
    def find_path(self, graph, v1, v2, visited):
        print(f"v1: {v1} v2: {v2}")
        if v1 in visited:
            return -1 
        
        if v1 == v2:
            return 1
        
        visited.add(v1)
        
        for nb in graph[v1]:
            nb_weight = graph[v1][nb]
            nb_path = self.find_path(graph, nb, v2, visited)
            if nb_path != -1:
                result = nb_weight * nb_path
                return result 
        
        return -1                 
    
    
    def buildGraph(self, edges, weights):
        graph = {}
        for i, [v1, v2] in enumerate(edges):
            if v1 not in graph:
                graph[v1] ={}
            graph[v1][v2] = weights[i]
            
            if v2 not in graph:
                graph[v2] = {}
            graph[v2][v1] = 1/weights[i]
        
        return graph 
    
    
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# queries = [["b","a"]]

s = Solution()
print(s.calcEquation(equations, values, queries))