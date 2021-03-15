
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. check if it is None
        if s is None:
            return False
        
        # 2. two pointers to check 
        left, right = 0, len(s)-1

        while left < right:
            # make sure to go to the valid char (digit or alpha) and stop there 
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1

            # lower each char and compare if lower version are equal or not 
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            # continue to move 
            left += 1
            right -= 1
            
        return True 

    def is_valid(self,char):
        return char.isdigit() or char.isalpha()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) is 0 or len(s) is 1:
            return True
        
        # Two pointers from left and right 
        ptr_one = 0
        ptr_two = len(s) - 1
        
        # lower all characters in string 
        s = s.lower()
  
        while (ptr_one <= ptr_two):
            
            # check if only letter or number 
            if not s[ptr_one].isalnum():
                ptr_one+=1
                continue
            elif not s[ptr_two].isalnum():
                ptr_two-=1
                continue
            if s[ptr_one] != s[ptr_two]:
                return False
            ptr_one+=1
            ptr_two-=1
        return True

# Time: O(n)
# Space:O(1)
