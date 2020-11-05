# 1. Recursion with Memoization

# Here is the algorithm.

# Clean up the input by replacing more than one star in a row by a single star: p = remove_duplicate_stars(p).

# Initiate the memoization hashmap dp.

# Return the helper function with a cleaned input: helper(s, p).

# helper(s, p):

# If (s, p) is already known and stored in dp, return the value.

# If the strings are equal p == s, or the pattern matches whatever string p == '*', add dp[(s, p)] = True.

# Else if p is empty, or s is empty, add dp[(s, p)] = False.

# Else if the current characters match p[0] == s[0] or p[0] == '?', then compare the next ones and add dp[(s, p)] = helper(s[1:], p[1:]).

# Else if the current pattern character is a star p[0] == '*', then there are two possible situations: the star matches no characters, and the star matches one or more characters. dp[(s, p)] = helper(s, p[1:]) or helper(s, p[1:]).

# Else p[0] != s[0], add dp[(s, p)] = False.

# Now that the value is computed, return it dp[(s, p)].


class Solution:
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 
        
    def helper(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False

        # ? skip because it represents single char 
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = self.helper(s[1:], p[1:])

        # if *, two options: 
        # 1. * matchs no char
        # 2. * represents one or more chars
        elif p[0] == '*':
            dp[(s, p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]
        
    def isMatch(self, s, p):
        p = self.remove_duplicate_stars(p)
        # memoization hashmap to be used during the recursion
        self.dp = {}
        return self.helper(s, p) 

 # Time: O(min(S,P)) for best case, O(2^min(S,P/2)) for worst case. where S and P are lengths of the input string
 # and the pattern correspondingly. The best case is quite obvious, let's estimate the worst case. 
 # The most time consuming is the situation where recursion forms the tree on the star character 
 # in the pattern. In this situation 2 branches are executed : helper(s, p[1:]) and helper(s[1:], p). 
 # The maximum number of stars in the pattern after data cleanup is P/2

 # Space:O(2^min(S,P/2)) to keep memoization hashmap and recursion stack 


# 2. DP 
# https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            # char is empty, and p is * then it is true until we find all of *, to remove multiple * 
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

# Time: O(SP) where S and P are lengths of the input string and the pattern correspondingly.
# Space:O(SP) to keep matrix


# 3. Backtracking
# https://leetcode.com/problems/wildcard-matching/solution/

# There is no need to compute the entire matrix, and i.e. to check all the possibilities for each star :

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
 
        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern 
            elif star_idx == -1:
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        # The remaining characters in the pattern should all be '*' characters
        return all(x == '*' for x in p[p_idx:])

# Time: O(min(S,P))
# Space:O(1)




