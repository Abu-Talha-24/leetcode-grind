class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n, m = len(haystack), len(needle)
        first = -1
        i = 0
        while i < n:
            j = 0
            start = i
            while i < n and j < m and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m : 
                first = min(first, i - m ) if first != -1 else i - m
            elif j > 0:
                i = start + 1
            else:
                i += 1
        
        return first
            
        
        
        