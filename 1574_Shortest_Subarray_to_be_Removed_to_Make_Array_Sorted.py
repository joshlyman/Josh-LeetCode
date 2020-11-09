# Consider, for example, if arr = [1,2,3,10,4,2,3,5]

# The monotone non-decreasing prefix is [1,2,3,10]
# The monotone non-decreasing suffix is [2,3,5]
# We'll consider the following situations in the merge part:
# i. If we take [1] from the prefix, then we can attach [2,3,5] from the suffix to it
# ii. If we take [1,2] from the prefix, then we can attach [2,3,5] from the suffix to it
# iii. If we take [1,2,3] from the prefix, then we can attach [3,5] from the suffix to it
# iv. If we take [1,2,3,10] from the prefix, then we can attach [] from the suffix to it
# We exhaust all possible ways to concatenate the prefix and suffix using two pointers and choose the longest among all possible concatenated results. Now that we know what are the maximum number of elements we get to keep, we immediately know what is the shortest subarray to remove. I've made some small changes to op's code on part 3 so that (hopefully) you can see more clearly how the pointers method is being used here:

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0 
        r = len(arr)-1
        
        # get 2 subarrays from left and right 
        while l < r and arr[l+1]>=arr[l]:
            l+=1
        
        # means whole array is sorted 
        if l == len(arr)-1:
            return 0
        
        while r >0 and arr[r]>=arr[r-1]:
            r-=1
        
        # l means l+1 elements so need to use len(arr)-l-1
        # current min elements to remove between these 2 subarrays
        removeNum = min(r,len(arr)-l-1)
        
        # merge 2 subarrays 
        # make i as the left pt again to merge 2 subarrays 
        for i in range(l+1):
            if arr[i] <= arr[r]:
                removeNum = min(removeNum, r - i - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return removeNum
        

# Time: O(N)
# Space:O(1)