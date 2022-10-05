class Solution:
    def jump(self, nums: List[int]) -> int:
        
        count = 0
        distance = 0
        curr_pos = 0
        
        for i in range(len(nums)-1):
            distance = max(i+nums[i],distance)
            if curr_pos == i:
                curr_pos = distance
                count+=1
        return count
    
        def jump2(self, nums: List[int]) -> int:
            res = 0
            l = r = 0
            jumpCount = 0
            while r < len(nums)-1:
                maxJump = 0
                for i in range(l, r+1):
                    maxJump = max(maxJump, i + nums[i])
                l = r+1
                r = maxJump
                jumpCount += 1
            return jumpCount