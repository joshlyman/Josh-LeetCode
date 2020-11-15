"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# Line Swap

# first sort 
# then merge intervals 
# then find free time interval between merged intervals 


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten the given intervals.
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]
        
		# Sort the intervals by starting time which is a key part of this soln. and indentifying overlap.
        ints.sort(key = lambda x:x.start)
        
		# Now we want to merge intervals (the continuous periods of being busy).
        merged = []
        for i in ints:
		    # If we have no intervals in our list or the current task starts after the previous one ends.
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
			    # We know that the start time intersects the start,end of the previous task, so we take the max ending time.
				# As this will be a merged, continuous busy period.
                merged[-1].end = max(i.end, merged[-1].end)

        # Now we have our merged intervals we can look at the time between the merged 
		# intervals as these will be the free time for the employee. 
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
			
		# Now we're left with intervals of free time.
        return free

# Time: O(ClogC), C is # of intervals 
# Space:O(C)

# Heap 

# comparing with previous getting intervals across all, we can compare each interval of employee one by one 

# Say we are at some time where no employee is working. That work-free period will last until the next time some employee has to work.
# So let's maintain a heap of the next time an employee has to work, and it's associated job. When we process the next time from the heap, we can add the next job for that employee.

# Keep track of the latest time anchor that we don't know of a job overlapping that time.
# When we process the earliest occurring job not yet processed, it occurs at time t, by employee e_id, and 
# it was that employee's e_jx'th job. If anchor < t, then there was a free interval Interval(anchor, t).



# first load each emp's first job interval into heap, then pop the earliest time interval
# then update anchor with end time of interval to compare with next start time
# then load next job interval to heap 
class Solution(object):
    def employeeFreeTime(self, avails):
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in avails for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))

            # [1,3] -> anchor is 3, 3>2 in [2,5], so not attend, anchor is 5
            #  next is [6,7], 5<6, attend [5,6]
            anchor = max(anchor, avails[e_id][e_jx].end)
            if e_jx + 1 < len(avails[e_id]):
                heapq.heappush(pq, (avails[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans

# Time: O(ClogN), C is # of intervals, N is # of employee  
# Space:O(N)






