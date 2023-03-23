class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
    
        n = len(arr)
        
        num = 1
        i = 0
        while k > 0:
            if i < n:
                if num == arr[i]:
                    i += 1
                else: # missing number
                    k -= 1
            else:
                k -= 1
            num += 1
            
        return num - 1
            
            