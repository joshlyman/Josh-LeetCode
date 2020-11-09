class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)//4
        
        for i in range(len(arr)):
            
            # which means char has more than 4 of them 
            if arr[i] == arr[i+n]:
                return arr[i]

# Time: O(N) for worst case, average is O(logN)
# Space:O(1)