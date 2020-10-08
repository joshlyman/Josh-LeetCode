class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interArray = []
        
        for i in nums1:
            if i in nums2:
                interArray.append(i)
                nums2.remove(i)
        
        return interArray

# Fast version:

# from collections import Counter
# class Solution:    
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return (Counter(nums1) & Counter(nums2)).elements()
