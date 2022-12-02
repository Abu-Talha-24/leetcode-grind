class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        
        print( sorted(list(cnt1.values())), sorted(list(cnt2.values())) )
        
        
        return sorted(list(cnt1.values())) == sorted(list(cnt2.values())) and set(cnt1.keys()) == set(cnt2.keys())
        