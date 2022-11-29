class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        hp = []
        
        for el in freq:
            count = freq[el]
            
            heapq.heappush(hp, (count, el))
            
            while (len(hp) > k):
                heapq.heappop(hp)
            
        
        return [val[1] for val in hp]
            
            
        
        
        
        
            
            