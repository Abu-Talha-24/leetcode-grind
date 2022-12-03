class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        charset = set()
        l = 0
        
        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        
        return res
            
            
            
        
        