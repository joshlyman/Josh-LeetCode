class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup  = {}
        lookup['('] = ')'
        lookup['['] = ']'
        lookup['{'] = '}'
        
        for para in s:
            if para in lookup:
                stack.append(para)
            elif len(stack) == 0:
                return False 
            elif lookup[stack.pop()]!= para:
                return False 
        
        return len(stack) == 0  

# Time: O(n)
# Space: O(n)