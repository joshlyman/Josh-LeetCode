class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # essentially a two sum but use dict to store th remainder 
        
        remainders = collections.defaultdict(int)
        ret = 0 
        
        # either t%60 == 0 or find 60-t %60 and t%60 
        for t in time:
            if t%60 == 0:
                ret+=remainders[0]
            else:
                ret+=remainders[60-t%60]
            remainders[t % 60] +=1
            
        return ret 

# Time: O(N)
# Space:O(1), because the size of the array remainders is fixed with 60.