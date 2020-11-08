class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""]*len(s)
        for idx,si in enumerate(s):
            res[indices[idx]] = si 
        return "".join(res) 
        
# Time: O(N)
# Space:O(N)      
        
        