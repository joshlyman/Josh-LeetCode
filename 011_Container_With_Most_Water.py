class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        start = 0
        end = len(height)-1
        
        while start < end:
            area = (end-start)*min(height[end],height[start])
            
            if area > maxarea:
                maxarea = area
            
            if height[end]>height[start]:

                # explore new start to increasing height of start 
                start+=1
            else:
                end-=1
         
        return maxarea 

# Time: O(n)
# Space:O(n)