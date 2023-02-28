class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the possible ranges of k is 1..n
        n = max(piles)
        l, r = 1, n
        
        # n is answer in worst case
        res = n
        
        # calculate total time needed to eat with each 'k'(per hour eating)
        while l <=r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            elif hours >= h:
                l = k + 1
        
        return res
        