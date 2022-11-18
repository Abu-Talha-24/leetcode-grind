class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hm = {}
        
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] = -1
            else:
                hm[s[i]] = i
        
        for val in hm:
            if hm[val] >= 0:
                return hm[val]
        
        return -1
        
            
            