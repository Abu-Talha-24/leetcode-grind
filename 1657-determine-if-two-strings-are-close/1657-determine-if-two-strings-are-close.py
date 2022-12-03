class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        
        c1 = Counter(w1)
        c2 = Counter(w2)
        
        return c1.keys()==c2.keys() and sorted(c1.values()) == sorted(c2.values())
    