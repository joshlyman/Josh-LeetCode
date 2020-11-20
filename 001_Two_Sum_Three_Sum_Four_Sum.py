# 2 sum 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vis = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in vis:
                return [vis[diff], i]
            vis[num] = i

# 2 sum II

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]


# 3 sum 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            L, R = i + 1, n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == 0:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]: 
                        L += 1
                    while R > L and nums[R] == nums[R + 1]: 
                        R -= 1
                elif temp > 0:
                    R -= 1
                else:
                    L += 1
        return ans

# 3 sum closet 

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = ans_diff = 0x7fffffff
        n = len(nums)
        for i in range(n - 2):
            L, R = i + 1, n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == target:
                    return target
                elif temp > target:
                    R -= 1
                else:
                    L += 1

                diff = abs(temp - target)
                if diff < ans_diff:
                    ans, ans_diff = temp, diff
        return ans

# 4 sum 
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: 
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: 
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: 
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target: 
                    continue
                L, R = j + 1, n - 1
                while L < R:
                    temp = nums[i] + nums[j] + nums[L] + nums[R]
                    if temp == target:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]: 
                            L += 1
                        while R > L and nums[R] == nums[R + 1]: 
                            R -= 1
                    elif temp > target:
                        R -= 1
                    else:
                        L += 1
        return ans

