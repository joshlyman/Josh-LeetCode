class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq 
        
        # each time pop 2 minimum number from sticks and get res, then push sum of 2 into sticks  
        res = 0
        heapq.heapify(sticks)
        
        while len(sticks)>1:
            x,y = heapq.heappop(sticks),heapq.heappop(sticks)
            res += x+y
            heapq.heappush(sticks,x+y)
        
        return res 
            
# Time: O(NlogN)
# Space:O(N)