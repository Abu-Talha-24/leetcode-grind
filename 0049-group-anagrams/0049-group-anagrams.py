class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        # Complexity : O (m * n)
        
        res = defaultdict(list) # charCount to list of anagrams
        
        for s in strs:
            count = [0] * 26  # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
            
        return res.values()
                
                