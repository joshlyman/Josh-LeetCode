# Bubble Sort 

# Find the largest element A[i], reverse A[0:i+1], making the current largest at the head of the array, then reverse the whole array to make A[i] at the bottom.
# Do the above again and again, finally we'll have the whole array sorted.
# eg:

# [3,1,4,2] (input array)
# [4,1,3,2] -> [2,3,1,4] (current maximum 4 is placed at the bottom)
# [3,2,1,4] -> [1,2,3,4] (current maximum 3 is placed at the bottom)
# [2,1,3,4] -> [1,2,3,4] (current maximum 2 is placed at the bottom)
# [1,2,3,4] -> [1,2,3,4] (current maximum 1 is placed at the bottom)
# done!

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n):
            
            # find max from first n-i elements 
            cur_max = max(arr[0:n-i])
            j = 0
            
            # find the index of this max value 
            while arr[j] != cur_max:
                j += 1
            
            # j is the index of the max value, there are j+1 elements until the max
            # reverse first j+1 elements
            arr[:j+1] = reversed(arr[:j+1])
            res.append(j+1)
            
            # reverse all first n - i elements
            arr[:n-i] = reversed(arr[:n-i])
            
            res.append(n-i)
        return res

# Time: O(N^2)
# Space:O(N)