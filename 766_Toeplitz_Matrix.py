# Approach #1: Group by Category
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
        
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

# Time: O(MxN)
# Space:O(M+N)



# Approach 2: Compare With Top-Left Neighbor
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

# Version 2
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(matrix[i][j] == matrix[i+1][j+1] for i in range(len(matrix)-1) for j in range(len(matrix[0])-1))
    
# Time: O(MxN)
# Space:O(1)

# follow up
# https://leetcode.com/problems/toeplitz-matrix/discuss/179882/Follow-up-questions
