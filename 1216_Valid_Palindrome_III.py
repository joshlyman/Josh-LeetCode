# Same with Edit distance, where only deletion is allowed between s and reversed(s)

# DP 

# if one of them is empty we have to delete the entire other
# if last character is the same then no need to delete any of these last 2
# if last characters are not the same then delete either or
# the distance == total number of deletions in one string + total number of deletions in the other
# implies it has to be <= 2 * k
# (removing at most k in each)

# dp(i,j) is the edit distance of s1[:i] and s2[:j] (i.e. the number of operations to make s1[:i] and s2[:j] the same)
# dp(i,j) = dp(i-1,j-1) if s1[i-1]==s2[j-1]
# dp(i,j) = 1+min(dp(i-1,j), dp(i,j-1)), if s1[i-1]!=s2[j-1]
# dp(0,j) = j and f(i,0) = i

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        
        # initialization 
        dp = [[0] * (n + 1) for _ in range(n + 1)] 

        for i in range(n+1):
            dp[i][0] = i
       
        for j in range(n+1):
            dp[0][j] = j
        
        # reversed string     
        rs = "".join(reversed(s))
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rs[j-1]:
                    # same with previous 
                    dp[i][j] = dp[i-1][j-1]
                else:
                	# delete s[i-1] or rs[j-1]
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]) 
        
        # distance between s and reversed s is less than 2K
        return dp[n][n] <= 2*k

# Time: O(N)
# Space:O(N)
