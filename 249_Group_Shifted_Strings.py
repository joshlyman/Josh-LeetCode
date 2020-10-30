class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
 
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
            
        return list(hashmap.values())
        
 # Time: O(ab) where a is the total number of strings and b is the length of the longest string in strings.
 # Space:O(N)       
        
    
    
