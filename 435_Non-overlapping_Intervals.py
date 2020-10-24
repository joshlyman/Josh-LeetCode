# A classic greedy case: interval scheduling problem.

# The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
# This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
# E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

# Therefore, we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
    	# current earliest ending time 
        end = float(-inf)
        count = 0
        
        # sort based on end time 
        for s,e in sorted(intervals,key=lambda x:x[1]):
            
        	# if current start time is earlier than end time, that means overlap, need to remove
            if s <end:
                count+=1
            # if not earlier, then we update the current earliest ending time: end  
            else:
                end = e 
        
        return count 

# Time: O(N)
# Space:O(1)