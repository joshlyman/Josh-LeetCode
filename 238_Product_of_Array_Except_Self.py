class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # simply way is to use total product divided by self, but we are not allowed to use division 
        
        # 1. calculate 2 arrays to store each product on the left or light, then each get each element in left and right arrays to product: O(N), space is O(N) 
        
        # 2. to get O(1) space, based on 1, we can just use left array to get final except self array by producting right elements         
        p = 1
        n = len(nums)
        
        # build left product array 
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        
        # update left array using right product
        p = 1
        
        # range(n-1,-1,-1) means start from end to the beginning 
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

# Time: O(N)
# Space:O(1): output is not included inside based on definition