# DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(n):
            if f[i]:
                for j in wordDict:
                    l = len(j)
                    if s[i:i+l] == j:
                        f[i+l] = True
        return f[n]

# Time: O(N^2)
# Space:O(N)


# BFS and DFS
# Starts with string s. For each string visited, chop off front of string if it starts with a word in the dictionary and adds the shortened string to the queue or stack. If string becomes empty, that means word break succeeded. Keep a set of seen string states to avoid duplicate work.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

# Time: O(N^2)
# Space:O(N)