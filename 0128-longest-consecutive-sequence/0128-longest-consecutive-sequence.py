class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        minHeap = nums
        res = 0
        count = 0
        heapq.heapify(minHeap)
        start = heapq.heappop(minHeap)
        while(minHeap):
            num = heapq.heappop(minHeap)
            if num == start:
                continue
            if num - start == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
            start = num
        
        return res+1
                
            
            
            
        