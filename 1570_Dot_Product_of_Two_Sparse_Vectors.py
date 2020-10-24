class SparseVector:
    def __init__(self, nums: List[int]):
        # only store non-zero values in dict 
        
        self.dictnums = {}
        for i,x in enumerate(nums):
            if x:
                self.dictnums[i] = x 
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self, vec
        
        res = 0
        for i in self.dictnums:
            if i in b.dictnums:
                res+=a.dictnums[i]*b.dictnums[i]
        return res 
    
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


# Time: O(N)
# Space:O(N)
       

# If one vector is sparse, and the other is not, we can update dotProduct() to iterate through the shorter:
# class SparseVector:

#     # as above

#     def dotProduct(self, vec):
#         a, b = self, vec
#         if len(a.m) > len(b.m):
#             a, b = b, a
#         return sum(a.m[i] * b.m[i] for i in a.m if i in b.m)

