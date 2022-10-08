class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def first_position():
            l = 0
            r = n - 1
            
            while (l <= r):
                mid = l + (r - l) // 2
                
                if nums[mid] == target:
                    if mid > 0 and nums[mid - 1] == target:
                        r = mid - 1
                    else:
                        return mid             
                
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
            
            return -1
        
        def last_position():
            l = 0
            r = n - 1
            
            while (l <= r):
                mid = l + (r-l) // 2
                
                if nums[mid] == target:
                    if mid < n-1 and nums[mid+1] == target:
                        l = mid + 1
                    else:
                        return mid
                    
                
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
            
            return -1
        
        return [first_position(), last_position()]
        
        
        
#         def first_position():
#             low, high = 0, len(nums)-1

#             while low <= high:
#                 mid = (low + high)//2
#                 if nums[mid] == target:
#                     if mid > 0 and nums[mid - 1] == target:
#                         high = mid - 1
#                     else:
#                         return mid             
#                 elif nums[mid] < target:
#                     low = mid + 1
#                 elif nums[mid] > target:
#                     high = mid - 1

#             return -1
    
#         def last_position():
#             low, high = 0, len(nums) - 1

#             while low <= high:
#                 mid = (low + high)//2 

#                 if nums[mid] == target:
#                     if mid < len(nums)-1 and nums[mid+1] == target:
#                         low = mid + 1
#                     else:
#                         return mid
#                 elif nums[mid] < target:
#                     low = mid + 1
#                 elif nums[mid] > target:
#                     high = mid - 1

#             return -1
    
#         return [first_position(), last_position()]