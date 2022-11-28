class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # minHeap gives out the lowest element
        
        minHeap = []
        
        for num in nums:
            heapq.heappush(minHeap, num)
            
            if len(minHeap) > k:
                heapq.heappop(minHeap) # pops the lowest element
        
        
        return minHeap[0]