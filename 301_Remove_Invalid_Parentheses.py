
# Refer from approach 2
# https://leetcode.com/problems/remove-invalid-parentheses/solution/

# brute force is to find:

# 1.if the expression is valid or not
# 2.if the total number of removed parentheses removed in the current recursion is less than the global minimum till now or not.

# instead we can reduce this problem to finding # of musplaced ( and )
# so we can only remove # of musplaced ( and )

# Optimization:
# The most important thing here is that we have completely gotten rid of checking if the number of parentheses removed 
# is lesser than the current minimum or not. The reason for this is 
# we always remove the same number of parentheses as defined by left_rem + right_rem at the start of recursion.

# DFS + Recursion 
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # left: misplaced # of ( 
        # right: misplaced # of )
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    # will reduce if meet a closing bracket )
                    left -= 1

        # set is used to remove duplicates 
        self.ans = set()

        # depth means current index 
        # left: # of (
        # right:# of )
        # left_rem: # of misplaced (
        # right_rem:# of misplaced )
        # cur: current valid parentheses 
        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(cur)
            else:

                # need to remove because left_rem > 0
                if s[depth] == "(" and left_rem > 0:
                    dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                
                # need to remove because right_rem > 0
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                
                # need to add becaue this is a char 
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
                
                # need to add because left_rem ==0 so this is valid 
                elif s[depth] == "(":
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
                
                # need to add because right_rem ==0 so this is valid 
                elif s[depth] == ")" and right < left:
                    dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

        # start to recursion DFS           
        dfs(0, 0, 0, left, right, "")
        return list(self.ans)


# Time: O(2^N)

# The optimization that we have performed is simply a better form of pruning. 
# Pruning here is something that will vary from one test case to another. 
# In the worst case, we can have something like ((((((((( and the left_rem = len(S) 
# and in such a case we can discard all of the characters because all are misplaced. 
# So, in the worst case we still have 2 options per parenthesis and that 
# gives us a complexity of O(2^N).


# Space:O(N)

# The space complexity remains the same i.e. O(N) as previous solution. 
# We have to go to a maximum recursion depth of N before hitting the base case. 
# Note that we are not considering the space required to store the valid expressions. 
# We only count the intermediate space here.



# BFS 
# Refer from https://leetcode.com/problems/remove-invalid-parentheses/discuss/75028/Short-Python-BFS
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # initialize a set with one element
        # set is used here in order to avoid duplicate element
        level = {s}
        while True:
            valid = []
            for elem in level:
                if self.isValid(elem):
                    valid.append(elem)
            if valid:
                return valid
            # initialize an empty set
            new_level = set()
            # BFS
            for elem in level:
                for i in range(len(elem)):
                    new_level.add(elem[:i] + elem[i + 1:])
            level = new_level
    
    def isValid(self,s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0



# Refer from: https://leetcode.com/problems/remove-invalid-parentheses/discuss/75057/44ms-Python-solution
# Scan from left to right, make sure count["("]>=count[")"].
# Then scan from right to left, make sure count["("]<=count[")"].
 class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:       
        
        removed = 0
        results = {s}
        count = {"(": 0, ")": 0}
        for i, c in enumerate(s):
            if c == ")" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(i - removed + 1):
                        if result[j] == ")":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                removed += 1
            else:
                if c in count:
                    count[c] += 1
        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed
        for ii in range(ll - 1, -1, -1):
            i-=1
            c = s[i]
            if c == "(" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(ii, ll):
                        if result[j] == "(":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
        return list(results)


# Time: O(2^N)
# Space:O(N)

