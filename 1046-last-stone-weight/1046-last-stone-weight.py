class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            print(stones)
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 == stone2:
                continue
            else:
                if stone1 > stone2:
                    stones.append(stone1-stone2)
                else:
                    stones.append(stone2-stone1)
            
        return stones[0] if len(stones) else len(stones)
                    
                    
            
        