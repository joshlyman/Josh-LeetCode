# As we iterate i over range(len(nums)), maintain a variable summ which records the cumulative sum of entries 
# up to index i (inclusive). Some subarray nums[i:j+1] has sum equal to k is equivalent to saying that the sum of 
# nums[:j+1] minus the sum of nums[:i] is equal to k. Hence we maintain a Hash map which records the value of 
# summ at each iteration. During each iteration, we also check whether summ - k occurs in previous iterations. 
# If it did occur, we calculate the difference between their indices, which is the length of the subarray with sum 
# equal to k. The maximum of all such differences yields the value of the solution.

# similar with 560, Both use accum sum and hashtable
# in 560, we use hashtable to record # of array for each sum, 
# in this case, we record the index of array
# so based on diff between next index and previous index, we know the length of subarray


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # for diff of 0, we record as -1
        dic = {0:-1}
        summ = 0
        maxlen = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic and i-dic[summ-k] > maxlen:
                maxlen = i-dic[summ-k]
            
            # store accum sum as key and index of accum sum in hash table 
            if summ not in dic:
                dic[summ] = i
        return maxlen

# Time: O(N)
# Space:O(N)