class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = presum = 0
        
        satisfaction.sort(reverse=True)
        
        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum >= 0:
                res += presum
            else:
                break
        
        return res