# Backtracking 

# Use the DFS helper function to find solutions recursively. A solution will be found when the length of queens is equal to n ( queens is a list of the indices of the queens).
# In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid. 
# We can use this information to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only.


# Refer from
# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms

# Basically since all slopes are either (-1) or (1) going up or down (we only care about 45/135 degree slopes, we are bascially taking a coord and 
# 	solving for the y intercept in the slop intercept for y = mx + b. This always transforms into two forms in our case since we have 
# 	two slopes. EITHER: y = (-1)x + b -> y = -x + b -> y + x = b OR y = 1x + b -> y = x + b -> y - x = b. So either on the up or down 
# 	slope you solve for where a point on this line would intercept the y axis. Something to note is even though a slope looks like 
# 	its going downward in a visual image of a 2d grid, you need to check if the indices are actually increasing, in programming we usually 
# 	draw our grids backwards where the y axis value increases as it grows downward. T

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            """
            temp = [["." * i + "Q" + "." * (n - i - 1) for i in queens]]
            for t in temp:
                for tt in t:
                    print(tt)
                print("\n")
            print("\n")
            """

            p = len(queens) # p is the index of row
            if p == n:

            	# finish all rows and 
                result.append(queens)
                return None
            for q in range(n): # q is the index of col 
                # queens stores those used cols, for example, [0,2,4,1] means these cols have been used
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    # find col and use DFS move to next row, if in the end len of row is not equal with # of queens, then we do not return it 
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []

        # 1: store valid visited queens 
        # 2: store invalid nodes of diagnal 1: y-x (y =x+b)
        # 3: store invalid nodes of diagnal 2: y+x (y =-x+b)
        DFS([], [], [])
        
        # Here sol is each row 
        # i in sol is each col 
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

# Time: O(N!): factorial N 
# Space:O(N)