# Solution:
# https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        result = []
        
        while i < len(A) and j <len(B):
            A_start = A[i][0]
            A_end = A[i][1]
            B_start = B[j][0]
            B_end = B[j][1]
            
            # crossing to find each overlapping 
            re_start = max(A_start,B_start)
            re_end = min(A_end,B_end)
            
            # must be <=, because [5,5] is also overlapping
            if re_start<=re_end:
                result.append([re_start,re_end])
            
            # check end value to see if A or B has been exhausted 
            if A_end < B_end:
                i+=1
            else:
                j+=1
            
        return result 
            
        

# Time: O(M+N), where M,N are the lengths of A and B respectively.
# Space:O(M+N), if we dont count the output result, it will be O(1)