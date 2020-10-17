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