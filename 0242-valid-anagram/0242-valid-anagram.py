class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        count1 = Counter([char for char in s])
        count2 = Counter([char for char in t])
        
        return count1 == count2