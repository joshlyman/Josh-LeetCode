# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         interArray = []
        
#         for i in nums1:
#             if i in nums2:
#                 interArray.append(i)
#                 nums2.remove(i)
        
#         return interArray

# Fast version:

# from collections import Counter
# class Solution:    
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return (Counter(nums1) & Counter(nums2)).elements()

# Fast version:

class Solution:    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return (Counter(nums1) & Counter(nums2)).elements()
        
        if len(nums1)> len(nums2):
            return self.intersect(nums2,nums1)
        
        lookup = collections.defaultdict(int)
        
        for i in nums1:
            lookup[i]+=1
            
        results = []
        for i in nums2:
            if lookup[i]>0:
                results.append(i)
                lookup[i]-=1
        
        return results

# Time: O(n)
# Space: O(n)