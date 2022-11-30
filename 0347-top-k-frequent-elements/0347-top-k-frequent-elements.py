class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        freq = Counter(nums)
        minHeap = []
        
        for el in freq:
            count = freq[el]
            heapq.heappush(minHeap, (count, el))
             
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        
        return [val[1] for val in minHeap]
            
            