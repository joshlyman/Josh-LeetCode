class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1

Time: O(N)
Space:O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

Time: O(N)
Space:O(1)