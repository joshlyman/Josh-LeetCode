# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/

# We perform a recursive solution. There are four cases for what the string might look like:

# empty
# [integer]
# [integer] ( [tree] )
# [integer] ( [tree] ) ( [tree] )
# When there is no '(', we are in one of the first two cases and proceed appropriately.
# Else, we find the index "jx" of the ')' character that marks the end of the first tree. 
# We do this by keeping a tally of how many left brackets minus right brackets we've seen. 
# When we've seen 0, we must be at the end of the first tree. The second tree is going to be the 
# expression S[jx + 2: -1], which might be empty if we are in case #3.


# Recursion + Stack 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        ix = s.find('(')
        if ix < 0: 
            # if not find, ix = -1
            return TreeNode(int(s)) if s else None

        bal = 0
        for jx, u in enumerate(s):
            if u == '(': 
                bal += 1
            if u == ')': 
                bal -= 1
            if jx > ix and bal == 0:
                break

        root = TreeNode(int(s[:ix]))
        root.left = self.str2tree(s[ix+1:jx])
        root.right = self.str2tree(s[jx+2:-1])
        return root

# Other solution 
# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/168839/Python-solution 

# Maintain a stack and a current num string as we traverse s from the left. Initialize stack = [] and num = "". 
# We divide s[i] into following cases:

# If s[i] is a digit or "-", we update num by num += s[i].
# If s[i] == "(" and nums non-empty, we assign stack[-1].left to nums if it has not yet been assigned, 
#  else we assign stack[-1].right to nums. 
# After this, we append nums to stack.

# If s[i] == ")":
# (i). If nums nonempty, we assign stack[-1].left to nums if it has not yet been assigned, 
# else we assign stack[-1].right to nums. Contrary to the previous case, we do not append nums to stack.
# (ii). If nums is empty, we do stack.pop() so that stack[-1] becomes the parent of the popped node.

# Iterative 
class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return
        stack = []
        num = ""
        for i in range(len(s)):
            if s[i].isdigit() or s[i] == "-":
                num += s[i]    
            elif s[i] == "(":
                if num:
                    node = TreeNode(int(num))
                    if stack:
                        if not stack[-1].left:
                            stack[-1].left = node
                        else:
                            stack[-1].right = node
                        stack.append(node)
                    else:
                        root = node
                        stack.append(node)
                    num = ""
            else: # s[i] == ")"
                if num:
                    node = TreeNode(int(num))
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    num = ""
                else:
                    stack.pop()
        return root if not num else TreeNode(int(num))

# Simplified
class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return
        stack = []
        num = ""
        for i in range(len(s)):
            if s[i].isdigit() or s[i] == "-":
                num += s[i]    
            elif num:
                node = TreeNode(int(num))
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                else:
                    root = node
                if s[i] == "(":
                    stack.append(node)
                num = ""
            elif s[i] == ")":
                stack.pop()
        return root if not num else TreeNode(int(num))



# Other solution

# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100404/Python-hack

# I change a string like '4(2(3)(1))(6(5))' to 't(4,t(2,t(3),t(1)),t(6,t(5)))' and then just let Python evaluate that (with the help of my TreeNode constructor).

def str2tree(self, s):
    def t(val, left=None, right=None):
        node, node.left, node.right = TreeNode(val), left, right
        return node
    return eval('t(' + s.replace('(', ',t(') + ')') if s else None

# DFS

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        ## RC ##
        ## APPROACH : RECURSION ##
        ## EDGE CASE : 1. NEGATIVE NODE VALUES ##
        ## 2. SINGLE NODE VALUES CAN BE MULTPLE DIGITS 12, 123..etc ##
        
        def dfs(s):
            if not s: return None                       # empty string
            
            start = 0
            while(start < len(s) and s[start] != "("):  # until our first brace, whole string is node value
                start += 1
            
            node = TreeNode(s[0:start])
            if len(s) == start : return node            # no more characters, single node
                        
            l, r = 0, 0
            for i in range(start, len(s)):
                if s[i] == "(": l += 1
                if s[i] == ")": r += 1
                if l == r: break
            
            node.left = dfs(s[start+1:i])
            node.right = dfs(s[i+2:-1])
            return node
        
        return dfs(s)

        
