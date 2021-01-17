class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        
        for i in strs:
            s = ""
            
            for j in sorted(i):
                s+=j
            
            if s not in anagrams:
                anagrams[s] = [i] 
            else:
                anagrams[s].append(i)
            
        return list(anagrams.values())

# Time: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. 
# The outer loop has complexity O(N) as we iterate through each string. 
# Then, we sort each string in O(KlogK) time.

# Space: O(NK)


# V2 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            
            if key not in d: 
                d[key] = [w]
            else:
                d[key].append(w)
            
        return d.values()

# Use letters dict to replace the tuple of string 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            
            if tuple(count) not in d:
                d[tuple(count) ] = [s]
            else:
                d[tuple(count) ].append(s)
        
        return d.values()
 
# Time: O(NK)
# Space:O(NK)       

