class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        i = 1
        while i <len(prices):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
            i+=1    
                
        return maxprofit 

# Time: O(n)
# Space:O(n)