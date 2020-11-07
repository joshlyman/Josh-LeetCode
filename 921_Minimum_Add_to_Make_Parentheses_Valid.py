# Keep track of the balance of the string: the number 
# of '(''s minus the number of ')''s. A string is valid 
# if its balance is 0, plus every prefix has non-negative balance.

# Now, consider the balance of every prefix of S. If it is ever negative (say, -1), 
# we must add a '(' bracket. Also, if the balance of S is positive (say, +B), we must add B ')' brackets at the end.


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        bal = 0
        res = 0
        for si in S:
            if si == "(":
                bal +=1
            else:
                bal -=1
            
            # bal must be >= 0
            # if bal = -1, means we need 1 more ( in prefix  
            # then we add to 0, make it be balanced 
            if bal == -1:
                res +=1
                bal +=1
        
        # if bal > 0, means ) is more, we need count ( 
        return res+bal

# Time: O(N)
# Space:O(1)
