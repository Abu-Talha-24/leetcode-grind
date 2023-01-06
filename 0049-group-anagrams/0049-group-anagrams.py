class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hm = defaultdict(list)
        
        for word in strs:
            letters = [0]*26            
            for char in word:
                letters[ord(char) - ord("a")] += 1
            
            hm[tuple(letters)].append(word)
        
        
        return hm.values()
            