class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        start = 0
        end = 0
        str_set = set()
        substr = ""
        res = ""
        
        if n == 0:
            return 0
        
        while(end < n):
            
            
            if s[end] not in str_set:
                substr += s[end]
                str_set.add(s[end])
                if end == n-1:
                    if len(substr) > len(res):
                        res = substr 
                end += 1
            elif s[end] in str_set :
                str_set = set()
                if len(substr) > len(res):
                    res = substr
                substr = ""
                start = end = start + 1
            
                
        return len(res)
                
        