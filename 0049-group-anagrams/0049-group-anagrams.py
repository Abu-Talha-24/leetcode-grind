class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for word in strs:
            hm = [0] * 26
            for c in word:
                hm[ord(c) - ord("a")] += 1
            
            res[tuple(hm)].append(word)
        
        return res.values()
        