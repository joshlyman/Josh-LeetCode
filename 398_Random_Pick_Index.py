class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = idx = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            
            # next is if num == target, then we start to count the element
            # but at the same time, we need to make sure idx can be any of previous location 
            if cnt == 0:
                idx = i
                cnt = 1
            else:
                # this random will already give me numbers
                # between 0 and cnt inclusive
                # so for 2nd number I am getting random number 0 and 1
                # so each having a probability of 1/2
                # similarly for three numbers it will be 1/3
                rnd = random.randint(0, cnt)
                if (rnd == cnt):
                    idx = i
                cnt += 1

        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)