class Solution:
    def longestPalindrome(self, s: str) -> str:
        # current palindrome 
        palindrome = ""
        
        for i in range(len(s)):
            # "aba" 
            len1 = len(self.getlongestPalindrome(s,i,i))
            
            if len1>len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i)
            
            # "abba"
            len2 = len(self.getlongestPalindrome(s,i,i+1))
            
            if len2>len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i+1)
            
        return palindrome
            
    # for each element, check left and right directions to see if it is a palindrome 
    def getlongestPalindrome(self,s,left,right):
        while left>=0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        
        return s[left+1:right]

# Time: O(N^2)
# Space: O(N)