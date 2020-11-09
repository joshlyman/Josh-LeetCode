class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return 
        
        stack = []
        
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        
        return "".join(stack)

# Time: O(N)
# Space:O(N-D), D is total length of duplicates 