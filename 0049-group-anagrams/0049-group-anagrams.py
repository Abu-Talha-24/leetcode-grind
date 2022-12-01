class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for word in strs:
            alpha = [0]*26
            for char in word:
                alpha[ord(char) - ord("a")] += 1
            
            res[tuple(alpha)].append(word)
        
        return res.values()
                
        