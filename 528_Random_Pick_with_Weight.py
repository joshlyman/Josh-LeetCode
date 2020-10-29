class Solution:

    def __init__(self, w: List[int]):
        
        # do the accumulative sum 
        
        self.accum_sums = []
        accum_sum = 0
        for weight in w:
            accum_sum+=weight
            self.accum_sums.append(accum_sum)
        self.total_sum = accum_sum

    def pickIndex(self) -> int:
        
        # do binary search to find the target zone 
        
        # generate a random float in [0,1]
        target = self.total_sum*random.random()
        low,high = 0,len(self.accum_sums)
        
        while low < high:
            mid = low + (high - low)//2
            if target > self.accum_sums[mid]:
                low = mid + 1
            else:
                high = mid
        
        # if use high, then for [0,1) return 1,but 1 is for next weight
        return low 
           
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Time: O(N): O(N) + O(logN)
# Space:O(N): O(N) + O(1)