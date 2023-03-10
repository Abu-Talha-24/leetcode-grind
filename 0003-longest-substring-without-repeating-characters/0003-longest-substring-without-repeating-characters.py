class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        chars = set()
        l = 0
        res = 0
        
        r = 0
        while r < n:
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1
            
        return res