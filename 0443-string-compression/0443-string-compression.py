class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars += " "  # use a dummy char to take care last char
        prev = 0
        l = 0
        
        for r in range(len(chars)):
            if chars[r] != chars[prev]:  # only take action when new char starts
                chars[l] = chars[prev]
                l += 1
                count = r - prev
                if count > 1:
                    for c in str(count):
                        chars[l] = c
                        l += 1
                prev = r
                
        return l
            
        