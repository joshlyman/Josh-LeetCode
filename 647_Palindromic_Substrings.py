
# Expand around center 
# Let N be the length of the string. The middle of the palindrome could be in one of 2N - 1 positions: 
# either at letter or between two letters.

# For each center, let's count all the palindromes that have this center. Notice that 
# if [a, b] is a palindromic interval (meaning S[a], S[a+1], ..., S[b] is a palindrome), then [a+1, b-1] is one too.

# For each possible palindrome center, let's expand our candidate palindrome on the interval 
# [left, right] as long as we can. The condition for expanding is left >= 0 and right < N and S[left] == S[right]. 
# That means we want to count a new palindrome S[left], S[left+1], ..., S[right].

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = left + j
                
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans
 
# Time: O(N^2), expansion takes O(N)
# Space:O(1)

# Expand around center using Recursion style
def countSubstrings(self, s: str) -> int:
    #similar to longest palindrome
    # will assume a char as center and also current char and the previous one as the center
    
    self.res = 0
    i = 0
    self.ln = len(s)
    while i < self.ln:
        # assume i is the center
        # means odd length palindrome
        self.helper(s, i, i)
        
        # assume i-1, i is the center
        # means even length palindrome
        self.helper(s, i-1, i)

        i += 1
    
    return self.res

def helper(self, s, left, right):
    while left >= 0 and right < self.ln and s[left] == s[right]:
        self.res += 1
        left -= 1
        right += 1




# Manacher's Algorithm

def countSubstrings(self, S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))

# Time: O(N)
# Space:O(N)


# DP
# https://leetcode.com/problems/palindromic-substrings/discuss/555333/Python-Dynamic-Programming-Solution 


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        
        # create a matrix to store info about the substring 
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # set single characters as palindromes
        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            res += 1
        
        # fill the matrix 
        # example1: "aaaaa"
        # [1, 1, 1, 1, 1]
        # [0, 1, 1, 1, 1]
        # [0, 0, 1, 1, 1]
        # [0, 0, 0, 1, 1]
        # [0, 0, 0, 0, 1]
        
        # example2: "cdaabaad"
        # [1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 1, 0, 0, 0, 0, 0, 1]
        # [0, 0, 1, 1, 0, 0, 1, 0]
        # [0, 0, 0, 1, 0, 1, 0, 0]
        # [0, 0, 0, 0, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0, 1, 1, 0]
        # [0, 0, 0, 0, 0, 0, 1, 0]
        # [0, 0, 0, 0, 0, 0, 0, 1]
        
        for col in range(1, len(s)):
            for row in range(col):
                
                # every two chars are palindromes as well
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
                
                # to determine if substring is a palindrome you should know 
                # a) if the inner substring is the palindrome and
                # b) if the outer characters match
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        
        # print matrix
        # for line in dp:
        #     print(line)
        
        return res
