# dp[d] is the minimum price up to dth day

# On each day in days, to make sure we have a pass, we either

# buy a 1-day pass on that day
# buy a 7-day pass 6 days ago
# buy a 30-day pass 29 days ago
# If we buy a 7-day pass, the price will be the cost at "dp[day - 7] + costs[1]", which is the minimum price 7 days ago + we buy a 7-day pass 6 days ago

# We can buy a 7-day pass or a 30-day pass on day 1. That's why we have "dp[max(d - 7, 0)]" and "dp[max(d - 30, 0)]" to handle first 30 days.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1) 
        days = set(days) # convert day to set for fast look up later
        for d in range(1, last_day + 1):
            # to make sure we have pass, we either buy a 1-d pass today, a 7-d pass 6 days ago, or a 30-d pass 29 days ago
            if d in days:
                dp[d] = min(costs[2] + dp[max(d - 30, 0)], costs[1] + dp[max(d - 7, 0)], costs[0] + dp[d - 1])
            else: # we don't buy pass on day not in days
                dp[d] = dp[d - 1]
        return dp[-1]

# Time: O(N)
# Space:O(N)