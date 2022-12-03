class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        maxHeap = [(-count,el) for el,count in freq.items()]
        heapq.heapify(maxHeap)
        
        res = []
        for i in range(k):
            ans = heapq.heappop(maxHeap)[1]
            res.append(ans)
        
        return res
            
            