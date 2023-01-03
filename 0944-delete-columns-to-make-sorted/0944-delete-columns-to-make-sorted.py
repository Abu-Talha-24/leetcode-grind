class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        count = 0
        prev = ''
        
        for i in range(m):  # 0, 1, 2, ## columns
            
            for j in range(n): # 0-0, 0-1, 0-2 ## rows
                word = strs[j]
                
                if j == 0: 
                    prev = word[i]
                elif word[i] < prev:
                    count += 1
                    print(word, i)
                    break
                else:
                    prev = word[i]

        
        return count
            