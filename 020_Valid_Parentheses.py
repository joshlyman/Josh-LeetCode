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

# V2
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
            elif lookup[stack.pop()]!=para:
                return False
        
        # check if stack pop up all items, otherwise will be Falase
        # return len(stack)==0
        
        if len(stack) ==0:
            return True
        else:
            return False