# Standard DP Problem  

# refer solution:
# https://leetcode.com/problems/edit-distance/solution/

# The idea would be to reduce the problem to simple ones. For example, there are two words, horse and 
# ros and we want to compute an edit distance D for them. One could notice that it seems to be more 
# simple for short words and so it would be logical to relate an edit distance D[n][m] with the lengths 
# n and m of input words.

# Let's go further and introduce an edit distance D[i][j] which is an edit distance between the first 
# i characters of word1 and the first j characters of word2.


# If the last character is the same, i.e. word1[i] = word2[j] then

# D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1] - 1)D[i][j]=1+min(D[i−1][j],D[i][j−1],D[i−1][j−1]−1)

# and if not, i.e. word1[i] != word2[j] we have to take into account the replacement of the last character during the conversion.

# D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])D[i][j]=1+min(D[i−1][j],D[i][j−1],D[i−1][j−1])

# So each step of the computation would be done based on the previous computation

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        # if one of strings is empty
        if n*m == 0:
            return n+m 
        
        # DP array: m+1 x n+1  
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # most important 
        # init boundaries
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
            
        # DP 
        for i in range(1,n+1):
            for j in range(1,m+1):
                left = dp[i-1][j]+1
                down = dp[i][j-1]+1
                if word1[i - 1] == word2[j - 1]:
                    left_down = dp[i - 1][j - 1] 
                else:
                    left_down = dp[i - 1][j - 1]+1 
                
                dp[i][j] = min(left,down,left_down)
        
        return dp[n][m]

# Time: O(NM)
# Space:O(NM)



# Complete solution
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition



# Recursion 
class Solution:
    def minDistance(self, word1, word2):
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

# Recursion with memoization 
class Solution:
    def minDistance(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else: 
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]


# DP

class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]






