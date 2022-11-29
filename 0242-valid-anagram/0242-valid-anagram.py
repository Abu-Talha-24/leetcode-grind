class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sstr = [c for c in s]
        tstr = [c for c in t]
        sstr.sort()
        tstr.sort()
        
        return sstr == tstr