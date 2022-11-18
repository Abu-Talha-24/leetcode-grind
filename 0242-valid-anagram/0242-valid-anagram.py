class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char1 = {}
        char2 = {}
        
        for char in s:
            char1[char] = char1.get(char, 0) + 1
        
        for char in t:
            char2[char] = char2.get(char, 0) + 1
        
        
        return char1 == char2
            
        