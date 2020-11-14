# https://leetcode.com/problems/regular-expression-matching/discuss/413571/Python-60ms-human-readable-DP-solution

# 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
# 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
# 3, If p.charAt(j) == '*': 
#    here are two sub conditions:
#                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
#                2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
#                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
#                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
#                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty

def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[0]*(lenP) for i in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
        	# '*' Matches zero or more of the preceding element.
            if p[j] == '*':
            	# in this case, a* counts as empty
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
            	# '.' Matches any single character.​​​​
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                # '*' Matches zero or more of the preceding element.
                # dp[i][j] = dp[i-1][j] : in this case, a* counts as multiple a 
                # dp[i][j] = dp[i][j-2] : in this case, a* counts as empty
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

        return bool(dp[-1][-1])

# Time: O(TP)
# Space:O(TP)

# V2
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
