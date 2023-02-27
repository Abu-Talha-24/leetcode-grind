# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # find the first occurence of bad(true) val
        # good good good bad bad
        # false false false true true
        
        l, r = 0, n
        
        while (l <= r):
            
            mid = (l+r) // 2
            
            ver = isBadVersion(mid)
            
            if ver is True:
                r = mid - 1
            elif ver is False:
                l = mid + 1
        
        return l
                