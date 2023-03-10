class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            
            if s1 != s2:
                # new = max(s1, s2) - min(s1, s2)
                new = min(s1, s2) - max(s1, s2)
                heapq.heappush(max_heap, new)
            
        # return max_heap
        return -max_heap[0] if max_heap else 0
                
            
            
        
        