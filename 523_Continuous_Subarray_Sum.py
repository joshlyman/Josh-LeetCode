class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = {}
        presum[0] = -1
        s = 0
        
        for i,num in enumerate(nums):
            s+=num
            if k!=0:
                # find out the group of current prefix sum value
                s%=k
            
            # check if there is a prefix sum value that is in the same group 
            # the current prefix sum value and have distance >= 2, because it must have at least 2 numbers inside 
            if s in presum:
                if i - presum[s]>=2:
                    return True 
            # put current prefix sum into map if it is not present
            else:
                presum[s] = i
        
        return False 

# Time: O(N)
# Space:O(min(N,K)), The HashMap can contain upto min(n,k) different pairings.