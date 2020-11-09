# Idea is to update the interval between replace the latest stored temperature and current highest temperature 
# use stack to store the index with current highest temperature and update it later when finding a higher one 
# if not find, then just keep using default 0 days 

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # default is 0 
        ans = [0]*len(T)
        stack = []
        # Iterative and put index with higer temperature to stack 
        # Everytime a higher temperature is found, we update answer of the peak one in the stack.
        for i,t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur    
            # store the index with current higher temperature
            stack.append(i)
        return ans 

# Time: O(N)
# Space:O(N)
