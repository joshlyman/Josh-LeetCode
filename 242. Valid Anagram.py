class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)
        
        if sCounter == tCounter:
            return True
        return False

# Time: O(N)
# Space:O(1), Although we do use extra space, the space complexity is O(1) because the table's size stays constant no matter how large n is.