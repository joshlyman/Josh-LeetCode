# Stack 
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            # . refers to the current directory, so pass now 
            if token in ('', '.'):
                pass
            # double period .. moves the directory up a level, go back 
            elif token == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

# Time: O(N), if there are NN characters in the original path. First, we spend O(N) trying to split the 
# input path into components and then we process each component one by one which is again an O(N) operation. 
# We can get rid of the splitting part and just string together the characters and form directory names etc. 
# However, that would be too complicated and not worth depicting in the implementation. The main idea of this 
# algorithm is to use a stack. How you decide to process the input string is a personal choice.


# Space:O(N), Actually, it's 2N because we have the array that contains the split components and then 
# we have the stack.