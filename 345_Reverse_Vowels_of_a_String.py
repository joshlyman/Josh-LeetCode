class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        
        # important: transfer s to list 
        s = list(s)
        left = 0
        right = len(s)-1
        
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
            elif s[left] not in vowels:
                left +=1
                continue 
            elif s[right] not in vowels:
                right -=1
                continue 
            
            left+=1
            right-=1
        
        return "".join(s) 

# Time: O(N)
# Space:O(1)