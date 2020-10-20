class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1.brute force is O(n^3), space: O(1)
        # for each subarray to get sum 
    
        # 2.use cumulative sum, get sum[j+1] - sum[i]: O(n^2), space: O(n)
        
        # 3.Based on epoch 1, without space, sum on the go: O(n^2), space: O(1)
        
        # 4.Hashmap: # of subarrays which has sum k is equal to sum[j] - sum[i]
            
        count,sumArray = 0,0
        d = {}
        
        d[0]=1
        
        for i in nums:
            sumArray+=i
            if sumArray-k in d:
                count+=d[sumArray-k]
            
            if sumArray not in d:
                d[sumArray]=1
            else:
                d[sumArray]+=1
                
        return count  

# Time: O(N)
# Space:O(N), Hashmap mapmap can contain upto nn distinct entries in the worst case.
        
        