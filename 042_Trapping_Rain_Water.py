# DP 

# https://www.youtube.com/watch?v=EIFpXEzFIj8&ab_channel=%E5%B0%8F%E5%B0%8F%E7%A6%8FLeetCode 
# Use DP to save the max bar from left to right and from right to left
# Two pass 


class Solution:
    def trap(self, height: List[int]) -> int:
        
        # edge case
        if not height:
            return 0
        
        leftMax = [0]*len(height)
        leftMax[0] = height[0]
        
        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1],height[i])
                
        
        rightMax = [0]*len(height)
        rightMax[len(height)-1] = height[-1]
        
        for i in range(len(height)-2,-1,-1):
            
            # here is i+1, not i-1 
            rightMax[i] = max(rightMax[i+1],height[i])
        
        res = 0
        for i in range(len(height)):
            # trapping water needs to - height[i] 
            res+=min(leftMax[i],rightMax[i]) - height[i]
            
        return res 
            
# Time: O(N)
# Space:O(N)


# Use two Pointers, MinMax problem: to update leftMax and rightMax 
class Solution:
    def trap(self, height: List[int]) -> int:
        
        # one pass, two pointers 
        leftMax = 0
        rightMax = 0
        
        # Two Pointers
        left = 0 
        right = len(height)-1
        
        res = 0
        # iterate from left to right and from right to left 
        while left <= right:
            if leftMax <= rightMax:
                
                # get the water in the top of the ground of left pt, but avoid neg number case: height is larger than max height 
                res += max(min(leftMax,rightMax) - height[left],0)
                # update leftMax with current height
                leftMax = max(leftMax,height[left])
                left+=1
            else:
                res += max(min(leftMax,rightMax) - height[right],0)
                
                # update rightMax with current height
                rightMax = max(rightMax,height[right])
                right-=1
            
        return res 

# Time: O(N)
# Space:O(1)        


# Another solution:
# https://leetcode.com/problems/trapping-rain-water/discuss/245162/Python-easy-to-understand-solution-one-pass-using-2-pointers

def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = right_max = water = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
                
        return water


