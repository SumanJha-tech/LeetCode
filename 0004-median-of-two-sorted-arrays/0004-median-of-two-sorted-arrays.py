class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            px = (low + high) // 2
            py = (m + n + 1) // 2 - px
            
            maxLeftX = float('-inf') if px == 0 else nums1[px - 1]
            minRightX = float('inf') if px == m else nums1[px]
            
            maxLeftY = float('-inf') if py == 0 else nums2[py - 1]
            minRightY = float('inf') if py == n else nums2[py]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found correct partition
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            
            elif maxLeftX > minRightY:
                high = px - 1
            else:
                low = px + 1
