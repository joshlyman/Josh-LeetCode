class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I":1,"V":5,"X":10,"L":50, "C":100, "D":500, "M":1000 }
        
        result = 0
        for i in range(len(s)):
            if i >0 and map[s[i]] > map[s[i-1]]:
                result += map[s[i]] - 2*map[s[i-1]]
            else:
                result += map[s[i]]
                
        return result 

 # Time: O(1)
 # Space:O(1)