https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation 

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # find rightmost index for each letter 
        rightmost = {letter: index for index,letter in enumerate(S)}
        
        left  = 0
        right = 0
        result = []
        
           # search each letter's rightmost index to split in this index because in next parts, these letters will not appear, which means appears in at most one part 
        
        for index,letter in enumerate(S):
            right = max(right,rightmost[letter])
            
            if index == right:
                # count # of letters in this part
                result.append(right-left +1)
                # move to next part 
                left = index +1
                
        return result 
        
# Time: O(N)
# Space:O(1)               
            
        
        
