class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Sliding Window
        charset = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])   # keep removing characters from left until the repeating char arrives
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1 )
        
        return res
            
            
        