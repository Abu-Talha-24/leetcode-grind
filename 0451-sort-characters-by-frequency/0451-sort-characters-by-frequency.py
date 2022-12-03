class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        
        freq = [ [k,v] for k,v in count.items() ]
        
        freq.sort(key=lambda x:x[1], reverse=True)
        
        res = ""
        for el in freq:
            res += el[0] * el[1]
        
        return res
            
        
        