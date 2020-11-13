class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(remain,comb,start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return 
            
            # not satify condition 
            elif remain <0:
                # exceed the scope, stop exploration.
                return 
            
            for i in range(start,len(candidates)):
                
                
                # # Very important here! We don't use `i > 0` because we always want to count the first element in this recursive step even if it is the same as one before. To avoid overcounting, we just ignore the duplicates after the first element.
                if i > start and candidates[i] == candidates[i-1]:
                    continue 
                
                # add the number into the combination
                comb.append(candidates[i])
                
                # dont give current number another chance, just moving on
                backtrack(remain-candidates[i],comb,i+1)
                # backtrack, remove the number from the combination
                comb.pop()
        
        backtrack(target,[],0)
        
        return results 

# Time: O(2^N)
# Let N be the number of candidates, so here should be total # of combinations 

# Space:O(N)