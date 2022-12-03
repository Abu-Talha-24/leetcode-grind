class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        arr = list(freq.items())
        arr.sort(key = lambda x:x[1], reverse=True)
        # arr = sorted(freq.items(), key=lambda kv: (kv[1], kv[0]) ) )

        res = ""
        for cnt in arr:
            res += cnt[0] * cnt[1]
            
        
        return res
            
        
        