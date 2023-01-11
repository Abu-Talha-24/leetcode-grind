class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        counts = [0] * n
        edges.sort(key=lambda x: -1 if x[1] == x[0] else 1)
        
        for edge in reversed(edges): # walk backwards
            
            if hasApple[edge[1]] or counts[edge[1]] > 0:
                counts[edge[0]] += 2 + counts[edge[1]] # forward and back + from previous node
                
            elif hasApple[edge[0]] or counts[edge[0]] > 0:
                counts[edge[1]] += 2 + counts[edge[0]] # forward and back + from previous node
        return counts[0]