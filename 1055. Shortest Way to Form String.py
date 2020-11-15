# Two pointers
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, minimum = 0, 1
        
        for c in target:
            
			# Get leftmost char after previously matched index
            i = source.find(c, i)

			# If not found
            if i == -1:
                
				# Get leftmost char from begining of string and increase number of concatenated string
                i = source.find(c)
                minimum += 1
                
				# if not found, then target can't be formed. Return -1
                if i == -1:
                    return i
                
            i += 1
                
            
                
        return minimum

# Time: O(MN)
# Space:O(MN)

# Binary Search
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sindex = {}
        for i, c in enumerate(source):
            if c not in sindex:
                sindex[c] = [i]
            else:
                sindex[c].append(i)
                
        for c in target:
            if c not in sindex:
                return -1
        
        ans = 1
        lst_si = -1
        for c in target:
            ind = bisect.bisect_right(sindex[c], lst_si)
            if ind == len(sindex[c]):
                ind = 0
                ans += 1
            lst_si = sindex[c][ind]
        return ans

# Time: O(NlogM)    
# Space:O(MN)    