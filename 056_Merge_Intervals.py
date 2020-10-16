class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # first sort each interval based on first element
        # python sort function needs O(nlogn) 
        intervals.sort(key=lambda x:x[0])
        
        merged = []
        
        for i in sorted(intervals,key = lambda i:i[0]):
            if merged and i[0] <=merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                merged.append(i)
        
        return merged 
                        
# Time: O(nlogn): because sorting takes nlogn, then simple linear scan takes n, so nlogn+n 
# Space:O(1): fixed space after sorting, o.w. will take O(n)


        
        
        
        