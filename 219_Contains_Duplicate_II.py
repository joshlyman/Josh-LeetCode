class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for ind, val in enumerate(nums):
            if val in hashmap and ind - hashmap[val]<=k:
                return True
            hashmap[val] = ind
        
        return False

# Time: O(N)
# Space:O(min(M,N))