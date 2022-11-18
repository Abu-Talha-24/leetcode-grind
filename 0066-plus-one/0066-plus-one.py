class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ''.join([str(d) for d in digits])
        
        total = int(s) + 1
        
        return [int(i) for i in str(total)]
        