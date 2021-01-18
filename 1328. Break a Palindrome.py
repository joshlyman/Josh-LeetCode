class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        # check half of strings to replace the non-a to a 
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        
        # it means all chars are "a", so have to replace the last a as b
        if palindrome[:-1]:
            return palindrome[:-1] + 'b' 
        else:
            return ""
            
# Time: O(N)
# Space:O(N)
        
