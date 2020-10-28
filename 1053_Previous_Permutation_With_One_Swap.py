class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        
        # The same technic to solve 31. Next Permutation
        # don't need to reverse the sequence
        # and [3,1,1,3] should be noticed
        
        
        i = len(A)-2
        while i > -1:
            
            # find the largest element i from end to beginning.
            if A[i] > A[i+1]:
                
                # from pivot to the end, find the largest element pivot after i, but i must be larger (not equal: 3113->1313) than pivot. 
                pivot = j = i+1
                while j <len(A) and A[i] > A[j]:
                    if A[j] > A[pivot]:
                        pivot = j  # the difference
                    j += 1
                
                # swap i with pivot 
                A[i], A[pivot] = A[pivot], A[i]
                break
            i -= 1
        return A
        

# Time: O(N)
# Space:O(1)