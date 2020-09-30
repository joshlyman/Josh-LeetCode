class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = []
        
        self.helper(n,n,"",result)
        
        return result
    
        
    def helper(self,l,r,item,result):
        
        # l and r means # of remaining parenthesis 
        
        if r < l:
            return 
        
        if l == 0 and r == 0:
            result.append(item)
            
        if l>0:
            self.helper(l-1,r,item+"(", result)
        
        if r>0:
            self.helper(l,r-1,item+")", result)

# Time: O(n)
# Space:O(1)