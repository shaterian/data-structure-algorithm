from collections import deque, defaultdict

graph = {
    "a":  ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

def dfs(graph, source):
    stack = [source]
    
    while stack:
        current = stack.pop()
        print(current)
        
        for nb in graph[current]:
            stack.append(nb)

def dfs_r(graph, source):
    print(source)
    for nb in graph[source]:
        dfs_r(graph, nb)

# identical to dfs iterative 
def bfs(graph, source):
    q = [source]
    
    while q:
        current = q.pop(0)
        print(current)
        
        for nb in graph[current]:
            q.append(nb)


def has_path_dfs(graph, src, dst):
    if src == dst:
        return True 
    
    for nb in graph[src]:
        if has_path_dfs(graph, nb, dst):
            return True 
        
    return False 


def has_path_dfs(graph, src, dest):
    
    q = deque([src])
    while q:
        current = q.popleft()
        if current == dest:
            return True
        
        for nb in graph[current]:
            q.append(nb)
    
    return False

def build_graph(edges):
    graph = {}
    for [a, b] in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
            


def undirected(edges, src, dest):
    graph = build_graph(edges)
    # visited = {}
    return has_path(graph, src, dest, visited=set())

def has_path(graph, src, dest, visited = set()):
    
    if src == dest:
        return True
    
    if src in visited:
        return False
    visited.add(src)
    
    for nb in graph[src]:    
        if has_path(graph, nb, dest, visited):
            return True 
    
    return False
     
def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    
    for nb in graph[current]:
        explore(graph, nb, visited)
    
    return True 

def connected_component(graph):
    visited = set()
    count = 0 
    for node in graph:
        if explore(graph, node, visited):
            count += 1 
    return count 

def explore_(graph, node, visited):
    if node in visited:
        return 0 
    visited.add(node)
    count = 1 
    for nb in graph[node]:
        count += explore_(graph, nb, visited)
    return count
    
    
def largest_component(graph):
    
    max_component = 0 
    visited = set()
    for node in graph:
        component_size = explore_(graph, node, visited)
        max_component = max(max_component, component_size)
        
    return max_component
        
def shortest_path(graph, src, dest):
    q = deque([(src, 0)])
    visited = set([src])
    while q:
        current, d = q.popleft()
        if current == dest:
            return d
        for nb in graph[current]:
            if nb not in q: 
                visited.add(nb)
                q.append((nb, d+1))
    return -1

def num_of_islands(matrix):
    
    DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]
    def dfs(i, j):
        if matrix[i][j] == 0:
            return 
        
        matrix[i][j] = 0
        for dr, dc in DIRECTIONS:
            r, c = i + dr, j + dc
            dfs(r, c)

    island_count = 0 
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                island_count += 1 
                dfs(i, j)
    return island_count        
         

def num_of_islands(grid):
    
    if not grid:
            return 0 
    m, n = len(grid), len(grid[0])
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
    def dfs(i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == "0":
            return 0 

        count = 1
        grid[i][j] = 0
        for dr, dc in directions:
            r, c = i + dr, j + dc
            count += dfs(r, c)
        return count 
    
    min_island_count = 0 
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                min_island_count = min(min_island_count, dfs(i, j))
    
    return min_island_count
         
         
bfs(graph, "a")
print(has_path_dfs(graph, "a", "g"))
edges = [["i", "j"], ["j", "k"], ["i", "k"]]
graph = build_graph(edges)
print(connected_component(graph))
print(undirected(edges, "i", "k"))
print(largest_component(graph))
print(shortest_path(graph, "i", "k"))




