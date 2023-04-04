class Solution:
    def partitionString(self, s: str) -> int:
        
        res = 0
        i = 0
        while i < len(s):
            uniq = set()
            while i < len(s) and s[i] not in uniq:
                uniq.add(s[i])
                i += 1
            
            res += 1
        
        return res
            
            