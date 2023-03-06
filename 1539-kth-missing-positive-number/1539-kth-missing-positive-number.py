class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        miss = []
        num = 1
        
        i = 0
        while i < len(arr):
            if num != arr[i]:
                miss.append(num)
                num += 1
            else:
                num += 1
                i += 1
        while len(miss) < k:
            miss.append(num)
            num += 1
        
        return miss[k-1]
            