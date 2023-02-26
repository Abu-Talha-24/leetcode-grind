class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        k = n - k  # calculating the index
        
        def quickSelect(l, r):
            pivot = nums[r] # select pivot as rightmost element
            p = l # pos starting from left
            
            # creating a partiion for <pivot and >pivot.
            for i in range(l, r):
                if nums[i] <= pivot: # if num is less than pivot
                    nums[p], nums[i] = nums[i], nums[p] # swap with pos
                    p += 1 
                
            # swap the pivot element with where pos last ended up at
            nums[p], nums[r] = nums[r], nums[p] 
            if p > k:
                return quickSelect(l, p-1) # quickselect on left parition
            elif p < k:
                return quickSelect(p+1, r) # quickselect on right partitoin
            else: # if p == k
                return nums[p]
        
            
        return quickSelect(0, n - 1)
        