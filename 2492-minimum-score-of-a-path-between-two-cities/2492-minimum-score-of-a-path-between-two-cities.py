class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
#         n = 4
#         # Adjacency Matrix -> Graph
#         [
#             [], # a, b, distance, city 'a' and 'b' 'distance'
#             [],
#             [],
#             [],
#         ]
        
#         # score of a path : return the min distance road, in the whole path from 1 to n
        
#         # Brute Force:
#             # 1. Find the minimum distance
#             # 2. Check if any one of the two nodes in the min distance are connected to the final node
#                     # DFS from the both nodes to find connectivity
#                     # if true:
#                         return
#                     # else: 
#                         find the next least distance
        
        # Adjacency List !
        adj = defaultdict(list) # node -> list of (neighbour, dist)
        
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))
            
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for nei, dist in adj[i]:
                res = min(res, dist)
                dfs(nei)
            
        
        res = float("inf")
        visit = set()
        dfs(1)
        return res
        
        
        