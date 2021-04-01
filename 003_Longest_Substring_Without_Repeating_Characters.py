# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        
        # pointer of sliding window, if find the char in window, then need to move pointer to right to remove all chars until remove this char  
        left = 0
        max_len = 0
        cur_len = 0 
        
        for ch in s:
            while ch in window:
                window.remove(s[left])
                left +=1
                cur_len -=1
        
            window.add(ch)
            cur_len +=1
            max_len = max(max_len,cur_len)
        
        return max_len 
        

# time: O(n)
# space: O(n)
