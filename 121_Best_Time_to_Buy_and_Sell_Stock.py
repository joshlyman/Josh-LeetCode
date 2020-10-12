class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # normal solution 
        
        min_price = inf 
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        
        return max_profit
    
        # Time: O(n)
        # Space:O(1)
        
        # DP
        
        # Define dp(i, j) as the the maximum profit on day i and status j.
        # We've bought a stock if status j equals to 0 and sold a stock if status j             equals to 1.
        # We'll get the recursion below:

    # dp(i, 0) = max(dp(i - 1, 0), -prices[i])
    # dp(i, 1) = max(dp(i - 1, 1), dp(i - 1, 0) + prices[i])
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
        # construct DP space with i as day and j as status 
#         n = len(prices)
#         dp = [[0] * 2 for _ in range(n + 1)]
        
#         # initial is -inf 
#         dp[0][0] = float('-inf')
#         for i, p in enumerate(prices, 1):
#             dp[i][0] = max(dp[i - 1][0], -p)
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + p)
#         return dp[-1][1]
        
        # DP needs more space: O(n)
    
        
        
        
        