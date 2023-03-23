class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        wires = len(connections)
        if wires < n - 1:
            return -1
        
        adj = defaultdict(list)
        visited = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        c = 0
        for node in range(n):
            if node not in visited:
                c += 1
                dfs(node)
        
        return c - 1