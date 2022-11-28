class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Complexity : O(nlogn) 
        
        stones = [-s for s in stones] # Making a max heap
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # ! Opposite signs as the values in heap are -ve
            if second > first:   #!
                heapq.heappush(stones, first - second)  #!
                    
                
        return abs(stones[0]) if len(stones) > 0 else len(stones)
                
        
                    
                    
            
        