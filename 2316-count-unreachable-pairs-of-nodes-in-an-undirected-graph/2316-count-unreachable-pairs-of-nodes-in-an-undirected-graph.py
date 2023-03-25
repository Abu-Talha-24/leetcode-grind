class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        visited = set()
        sizes = [0] * n
        
        for i in range(n):
            if i not in visited:
                sizes[i] = self.dfs(i, adjList, visited)
        
        ans = 0
        sum = 0
        for size in sizes:
            ans += sum * size
            sum += size
        
        return ans
    
    
    def dfs(self, node, adjList, visited):
        visited.add(node)
        size = 1
        for nei in adjList[node]:
            if nei not in visited:
                size += self.dfs(nei, adjList, visited)
        return size
        