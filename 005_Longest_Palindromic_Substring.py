class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        
        for i in range(len(s)):
            len1 = len(self.getlongestPalindrome(s,i,i))
            
            if len1>len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i)
            
            len2 = len(self.getlongestPalindrome(s,i,i+1))
            
            if len2>len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i+1)
            
        return palindrome
            
    
    def getlongestPalindrome(self,s,left,right):
        while left>=0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        
        return s[left+1:right]

# Time: O(n)
# Space: O(n)