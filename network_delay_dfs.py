from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        def build_graph(edges):
            graph = defaultdict(dict)
            for src, dest, travel_time in edges:
                graph[src][dest] = travel_time
            return graph 
        
        def dfs(node, current_time, visited, memo):
            if node in memo and current_time >= memo[node]:
                return memo[node]
            
            memo[node] = current_time
            visited.add(node)
            
            for neighbor, travel_time in graph[node].items():
                if neighbor not in visited:
                    dfs(neighbor, current_time + travel_time, visited, memo)
            
            visited.remove(node)
        
        graph = build_graph(times)
        memo = {}
        dfs(k, 0, set(), memo)
        if len(memo) < n:
            return -1
        max_time = max(memo.values())
        return max_time if max_time < float("inf") else -1
