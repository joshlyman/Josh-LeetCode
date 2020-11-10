# graph refer from:
# https://leetcode.com/problems/diagonal-traverse-ii/discuss/597741/Clean-Simple-Easiest-Explanation-with-a-picture-and-code-with-comments

# each diagonal is a level 1..N from top left to bottom right
# for each level, use a [] to store it
# since output is from bottom left to top right, so we need to reverse it 

def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]

# Time: O(N)
# Space:O(N)

# mine 
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        
        for i,r in enumerate(nums):
            for j,val in enumerate(r):
                # for each level, create a list to store 
                if len(res) <= i+ j:
                    res.append([])
                res[i+j].append(val)
        
        output = []
        for level in res:
            for v in reversed(level):
                output.append(v)
        
        return output 
