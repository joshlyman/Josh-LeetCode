class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        # remaining # of ( must be > # of )
        path = []
        results = []
        self.dfs(path,results,0,0,n,n)
        
        return results
        
        # path, para,results, remain # of (, remain # of ), current # of (, current # of )
        
    
    def dfs(self,path,results,leftCur,rightCur,leftRem,rightRem):
        if leftRem < 0 or rightRem < 0:
            return 
        
        if rightCur > leftCur:
            return  
        
        if leftRem == 0 and rightRem == 0:
            results.append("".join(path))
             
        path.append("(")
        self.dfs(path,results,leftCur+1,rightCur,leftRem-1,rightRem)
        path.pop()

        path.append(")")
        self.dfs(path,results,leftCur,rightCur+1,leftRem,rightRem-1)
        path.pop()

# https://www.jiuzhang.com/problem/generate-parentheses/
# https://leetcode.com/problems/generate-parentheses/solution/

# Time: O(4^n/sqrt(n))
# Space:O(4^n/sqrt(n))