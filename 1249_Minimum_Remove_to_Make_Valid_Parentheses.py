class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Remove a ")" if it is encountered when stack was already empty (prevent               negative balance). 
        # Remove a "(" if it is left on stack at end (prevent non-zero final balance).
        
        # use stack (list in python) to put(append) and pop(pop)
        
        
        # 1.Convert string to list, because String is an immutable data structure in    Python and it's much easier and memory-efficient to deal with a list for this task.
        # 2.Iterate through list, Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
        # 3.When we come across close parenthesis we pop an element from the stack. If the stack is empty we replace current list element with an empty string
        # 4.After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
        # 5.Convert list to string and return
        
        
        ls = list(s)
        stack = []
        for i in range(len(ls)):
            if ls[i] == '(':
                stack.append(i) 
            elif ls[i] == ')':
                if stack:
                    stack.pop()
                else:
                    ls[i]=''
       
        # iterate stack until empty redudant ( 
        while stack:
            ls[stack.pop()] = ''
        return "".join(ls)
        
#Time: O(n)

# Details see:https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/

#Space:O(n)      

# We are using a stack, set, and string builder, each of which could have up to n characters in them, and so require up to O(n)O(n) space.             
                
                
                
                
                
                
        
        