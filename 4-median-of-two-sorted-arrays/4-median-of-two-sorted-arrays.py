class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # A should be the smaller one
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        # log(min(m,n)))
        while True:
            i = (l + r) // 2 # pointer to A
            j = half - i - 2 # pointer to B
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float ("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # checking if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
        