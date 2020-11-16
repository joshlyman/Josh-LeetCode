# we do random swapping as shuffling
# in reset we need to both reset the array and original 
class Solution:
    import random 
    def __init__(self, nums: List[int]):
        self.array = nums
        
        # copy or we can do
        # self.original = nums[:]
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        
        self.array = self.original
        
        # back to original, reset 
        self.original = list(self.original)
        
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            
            # swap index with a next random index
            swap_indx = random.randrange(i,len(self.array))
            self.array[i],self.array[swap_indx] = self.array[swap_indx], self.array[i]
        
        return self.array
        
# Time: O(N)
# Space:O(N)       


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# V2
import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans