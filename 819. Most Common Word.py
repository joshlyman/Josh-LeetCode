class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for c in "!?',;.": 
            paragraph = paragraph.replace(c, " ")
        
        d = {}
        res = ""
        count = 0
        banned_words = set(banned)
        
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in d:
                d[word] += 1
            else:
                d[word] = 1
                
            if d[word] > count:
                count = d[word]
                res = word
        return res
        
        
# Time: O(N+M): N be the number of characters in the input string and M be the number of characters in the banned list.

# Space:O(N+M)


