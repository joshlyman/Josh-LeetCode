
# DFS 
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        
        def dfs(word):
            
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True 
                
                if prefix in d and dfs(suffix):
                    return True 
                
            return False
        
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res 

Time: O(NL), N words and each word has L length 
Space:O(NL^2)

# DFS with memoization 

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        memo = {}
        
        def dfs(word):
            
            if word in memo:
                return memo[word]
            memo[word] = False
            
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    memo[word] = True 
                    break 
                
                if prefix in d and dfs(suffix):
                    memo[word] = True 
                    break 
                
                if suffix in d and dfs(prefix):
                    memo[word] = True
                    break 
                
            return memo[word]
        
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res 