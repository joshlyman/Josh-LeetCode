class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge case: only 1 of 0: 0 
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True 
        
        # edge case: first 2 are both 0: 00xxx
        # count how many intervals    
        count = 0
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            count+=1
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count+=1
        
        # edge case: last 2 are 0: xxx00 
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            count+=1   
        
        return count >=n

# Time: O(N)
# Space:O(1)