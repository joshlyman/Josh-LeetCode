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