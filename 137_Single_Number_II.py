class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use hashset or hashmap will give O(N) space
        
        # Hashset
        # 3×(a+b+c)−(a+a+a+b+b+b+c)=2c
        # return (3 * sum(set(nums)) - sum(nums)) // 2
        
        # Time: O(N), Space: O(N)
        
        # Hashmap
#         from collections import Counter
#         class Solution:
#             def singleNumber(self, nums):
#                 hashmap = Counter(nums)

#                 for k in hashmap.keys():
#                     if hashmap[k] == 1:
#                         return k
        # Time: O(N), Space: O(N)
    
        # use bit manipulation will give O(1) space 
        
        # XOR is to be used to detect the bit which appears odd number of times: 1, 3, 5, etc.
        # 2^2 = 0, 2^2^2 = 2 
        
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
 
 # Time: O(N)
 # Space:O(1)       
        
        