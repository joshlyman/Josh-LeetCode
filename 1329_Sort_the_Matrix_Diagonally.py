# A[i][j] on the same diagonal have same value of i - j
# For each diagonal,
# put its elements together, sort, and set them back.

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # (1,4), i - j = -3
        # (1,3), (2,4), i -j = -2
        # (1,2), (2,3), (3,4), i-j = -1
        
        n, m = len(mat), len(mat[0])

        # create a dict and each element is a list 
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                
                # store element in each diagonal level 
                d[i - j].append(mat[i][j])
        
        # sort in reversed order: [3,2,1] 
        for k in d:
            d[k].sort(reverse=1)
        
        # pop each item: 1,2,3
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat

# or we can use sort and pop(0)

# for k in d.keys():
#             d[k].sort()
            
#         for i in range(rows):
#             for j in range(cols):
#                 mat[i][j] = d[i-j].pop(0)


# Time O(MNlogD), where D is the length of diagonal with D = min(M,N).
# Space O(MN)