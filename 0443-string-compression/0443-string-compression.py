class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars.append("")
        n = len(chars)
        p = 0
        count = 1
            
        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
            elif chars[i] != chars[i-1]:
                chars[p] = chars[i-1]
                if count > 1:                    
                    for num in str(count):
                        p += 1
                        chars[p] = num
                p += 1
                count = 1
        
        return p
            