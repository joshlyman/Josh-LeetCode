class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [ s.find(i) for i in s ] == [ t.find(i) for i in t ]
# Time: O(N)
# Space:O(1)

# another solution 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse = {}
        for i in range(len(s)):
            if s[i] not in mapping and t[i] not in reverse:
                mapping[s[i]] = t[i]
                reverse[t[i]] = s[i]
            if s[i] in mapping and mapping[s[i]] != t[i]:
                return False
            if t[i] in reverse and reverse[t[i]] != s[i]:
                return False
        return True

# Time: O(N)
# Space:O(N)