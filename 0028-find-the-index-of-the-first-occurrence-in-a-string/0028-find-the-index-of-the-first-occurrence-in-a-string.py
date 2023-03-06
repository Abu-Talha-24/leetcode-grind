class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        h, n = len(haystack), len(needle)
        res = -1
        
        i = 0
        while i < h:
            j = 0
            start = i
            while i < h and j < n and needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == n:
                res = min(res, start) if res != -1 else start
            else:
                i = start + 1
        
        
        return res
                