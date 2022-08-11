class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        hp = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for el in freq:
            count = freq[el]
            heapq.heappush(hp, (count, el))
            if len(hp) > k:
                heapq.heappop(hp)
        
        
        return [x[1] for x in hp]