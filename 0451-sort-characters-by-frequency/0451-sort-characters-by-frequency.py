class Solution:
    def frequencySort(self, s: str) -> str:
        
        hm = Counter(s)
        res = ""
    
        hmfinal = sorted(hm.items(), key=lambda x: -x[1])
        print(hmfinal)
        
        for char in hmfinal:
            res += char[0] * char[1]
        
        return res
            