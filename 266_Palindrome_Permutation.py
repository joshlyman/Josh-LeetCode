class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        
        for si in s:
            if si not in count:
                count[si] = 1
            else:
                count[si] +=1
        
        totalmod = 0
        for key in count:
            totalmod += count[key]%2 
        
        if totalmod>1:
            return False
        else:
            return True

Time: O(N)
Space:O(1), A mapmap of constant size(128) is used, not larger than 128 ASCII characters  


# V2
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True

Time: O(N)
Space:O(1), A mapmap of constant size(128) is used.


# V3
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        count = 0
        for item in s:
            dic[item] = dic.get(item, 0) + 1
            
            if dic[item]%2 == 0:
                count -=1
            else:
                count+=1
        
        if count >1:
            return False
        else:
            return True 

Time: O(N)
Space:O(1), A mapmap of constant size(128) is used.
      