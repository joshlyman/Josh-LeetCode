# 1.This problem is a manipulation of Two sum problem.
# 2. In this problem, order of numbers of a subsequence doesn't matter as we just have to consider max and min of subsequence.Therefore, a subsequence from i to j in original array is equivalent to array having same elements and same minimum and maximum value. For e.g consider, nums = [3,7,6,5] and target = 10.For eg, In this a subsequence [3,7,6] is equivalent to subsequence [3,6,7] of [3,5,6,7]. Therefore, result of nums is equal to result of sorted[nums].
# 3. For each index "i" in sorted_nums, find maximum "j" such that sorted_nums[i] + sorted_nums[j] <= target and j >= i.
# 4. From i+1 to j, we can either pick or leave each element.
# 5. Therefore, res += 2**(j-i)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        end = len(nums)-1
        
        nums.sort()
        for i in range(len(nums)):
            while nums[i] + nums[end] > target:
                if end > i:
                    end = end-1
                else:
                    return res % (10**(9)+7)
            res += pow(2, end - i)
        return res % (10**(9)+7)

# Time: O(NlogN), sorting takes O(NlogN)
# Space:O(1)