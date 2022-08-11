class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        
        res = [k for k,v in sorted(freq.items(), key=lambda item: item[1])]
        
        res = res[-1:-k-1:-1]
        
        return res