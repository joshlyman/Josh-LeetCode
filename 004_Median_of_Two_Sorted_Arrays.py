# median: Dividing a set into two equal length subsets, that one subset is always greater than the other.

# since it requres O(log) time, so we have to use binary search instead of using merge sort 
# because merge sort will take O(M+N) linear time 


# Refer from:
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms

# Good explanation video:
# https://www.youtube.com/watch?v=ScCg9v921ns&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90


# Binary search 
class Solution:
 	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        # when total length is odd, the median is the middle
        if (len1 + len2) % 2 != 0:
            return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
        else:
        # when total length is even, the median is the average of the middle 2
            middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
            middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
            return (middle1 + middle2) / 2

    # middle is kth element 
    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        
        # if nums1 ends earlier, it means remaining is in the nums2, so remaining number is k-start1 
        if start1 > end1:
            return nums2[k-start1]

        # if nums2 ends earlier, it means remaining is in the nums1, so remaining number is k-start2  
        if start2 > end2:
            return nums1[k-start2]
        
        # index of half of nums1 and nums2
        middle1 = (start1 + end1) // 2
        middle2 = (start2 + end2) // 2

        # middle value of nums1 and nums2
        middle1_value = nums1[middle1]
        middle2_value = nums2[middle2]
        
        # if sum of two median's indicies is smaller than k, which means still need to get more to find kth element
        # to see where is k located, nums1 or 2 
        if (middle1 + middle2) < k:
            # if nums1 median value bigger than nums2, then nums2's first half will always be positioned 
            # before nums1's median, so k would never be in num2's first half, so need to continue on nums2
            # so set up middle2+1 as new start for nums2 
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
            else:
                return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
        # if sum of two median's indicies is bigger than k, which means still we need to return back previous ones 
        # to see where is k located
        else:
            # if nums1 median value bigger than nums2, then nums2's first half would be merged 
            # before nums1's first half, thus k always come before nums1's median, then nums1's second half would never include k
            # so we need to decrease nums1, so set up middle1-1 as new end1 for nums1 
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)

# Time: O(log(M+N))
# Space:O(1)


