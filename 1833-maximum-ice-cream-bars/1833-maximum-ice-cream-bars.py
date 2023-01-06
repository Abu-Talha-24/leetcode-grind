class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        s, count = 0, 0
        
        for cost in costs:
            s += cost
            count += 1
            if s > coins:
                return count - 1
            elif s == coins:
                return count
        
        return count
            
            
            
            