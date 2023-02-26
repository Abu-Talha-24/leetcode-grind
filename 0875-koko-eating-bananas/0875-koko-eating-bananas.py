class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        res = r # the max element is the answer in worst case
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # hours needed to eat with that 'k'
                
            if hours <= h: # if it's less(valid) 
                res = min(res, k) # check if it's min
                r = k - 1 # to check if even less is possible
            else:
                l = k + 1 # to make it less hours increase k.
        
        return res