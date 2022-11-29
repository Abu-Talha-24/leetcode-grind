class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Time Complexity: O(n)
        
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            # check if start of sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
            
                
            
            
            
        