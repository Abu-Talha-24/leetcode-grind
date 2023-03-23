class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        
        def less(x):
            hours = 0
            for p in piles:
                hours += math.ceil(p / x)
            return hours <= h
        
        while l <=r :
            mid = (l + r) // 2
            
            if less(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l