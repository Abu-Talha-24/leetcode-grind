class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for i in range(n):
            num2 = target - nums[i]
            if num2 in dict1:
                return [dict1[num2], i]
            else:
                dict1[nums[i]]=i
    