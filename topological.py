from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build the graph representation of prerequisites
        graph = self.build_graph(prerequisites)
        
        topological_sort = []  # To store the final order
        V = set()              # Global visited set for fully processed nodes
        
        for node in range(1):
            visited = set()    # Reset for each path
            if node not in V:
                # Perform DFS and check for cycles
                if not self.dfs(node, graph, V, visited, topological_sort):
                    return []  # If a cycle is detected, return an empty list
        
        return topological_sort[::-1]  # Reverse the result for the correct topological order


    def dfs(self, node, graph, V, visited, topological_sort):
        
        print(f"Enter dfs {node}")
        if node in visited:
            print("Cycleeeeeee")
            return False  # Cycle detected
        if node in V:
            return True   # Node already fully processed
        
        # Mark the current node as visited in the current DFS path
        visited.add(node)
        
        # Explore neighbors
        for neighbor in graph[node]:
            if not self.dfs(neighbor, graph, V, visited, topological_sort):
                return False  # If a cycle is detected, propagate the failure
        
        # Finished processing all neighbors; mark node as fully visited
        print("Removeing {node} from visited")
        visited.remove(node)  # Remove from current DFS path (not needed anymore)
        print("Adding {node} to V ")
        V.add(node)           # Mark as fully processed
        topological_sort.append(node)  # Append to the result
        
        return True


    def build_graph(self, edge_list):
        graph = defaultdict(list)
        for dest, src in edge_list:
            graph[src].append(dest)  # Edge from src to dest (prerequisite relationship)

        return graph



s = Solution()
cycle = [[0,1],[1,2],[2,1]]
no_cycle = [[1,0], [2,1], [2,0]]
print(s.findOrder(3, no_cycle))