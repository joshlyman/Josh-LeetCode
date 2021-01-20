class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count =0
        for i in range(len(nums)):

        	# when meet different number, need to put the number back to increased pointers 
            if nums[count]!=nums[i]:

                count+=1
                nums[count]=nums[i]
        
        return count+1

#Time: O(n)
#Space:O(1)