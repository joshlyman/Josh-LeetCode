class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        # first do sorting on each 1st element 
        intervals.sort(key=lambda i: i[0])
        
        # need to consider intervals == []
        if len(intervals) == 0:
            return True
        
        for i in range(1,len(intervals)):
            
            # if [1,13] and [13,15] still is okay
            if intervals[i][0]< intervals[i-1][1]:
                return False
        # after scanning all, return True, not use else true here 
        return True 

# Time: O(nlogn): sorting takes nlogn and scanning takes n 
# Space:O(1)