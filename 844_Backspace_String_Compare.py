# Stack 
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S):
            stack = []
            for c in S:
                if c!='#':
                    stack.append(c)
                # it could be empty when 1st # shows up 
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(S) == build(T)

# Time: O(M+N)
# Space:O(M+N)

# Two Pointers 
# iterative in reversed string and get char from string 
# if chars are not equal then return false 

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        r1 = len(S) - 1 
        r2 = len (T) - 1
        
        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(S, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(T, r2)
            if char1 != char2:
                return False
        return True
        
    
    def getChar(self, s , r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r

# Time: O(M+N)
# Space:O(1)
