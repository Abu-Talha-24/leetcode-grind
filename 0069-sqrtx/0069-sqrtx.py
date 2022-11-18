class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        
        l, r = 1, x // 2
        
        while (l <= r):
            mid = (l + r) // 2
            
            prod = mid*mid
            
            if prod == x:
                return mid
            
            elif prod < x:
                l = mid + 1
            else:
                r = mid - 1
        
        
        return l-1
        