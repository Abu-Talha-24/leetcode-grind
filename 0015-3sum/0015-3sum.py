class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = set()
        nums.sort()
        
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                si = (nums[i], nums[j], nums[k])
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0 :
                    ans = (nums[i], nums[j], nums[k])
                    if ans not in res:
                        res.add(ans)
                    j += 1
                elif s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                
                
        return res
                
                
        