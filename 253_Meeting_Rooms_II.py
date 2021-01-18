class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # first sorting start time and end time 
        # two pointers, one is point to start time list, another point to end time, this means pointer to the first available room 
        
        starttime = sorted(x[0] for x in intervals)
        endtime = sorted(x[1] for x in intervals)
        
        e = 0
        roomnum = 0
        for i in range(len(starttime)):
            if starttime[i] < endtime[e]:
                roomnum +=1
            else:
                e +=1
        return roomnum 

# Time: O(NlogN), sorting takes nlogn
# Space:O(N)

# V2: my version 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # start 0  5  15
        # end   10 20 30
        
        start_time = sorted(x[0] for x in intervals)
        end_time = sorted(x[1] for x in intervals)
        
        eidx = 0
        roomnum = 0
        
        for sidx in range(len(start_time)):
            if start_time[sidx] < end_time[eidx]:
                roomnum +=1
            else:
                eidx +=1
        
        return roomnum 
        
# V2: use heap 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # start 0  5  15
        # end   10 20 30
        
        # use heap to track the end of meeting time 
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        
        free_rooms = []
        heapq.heapify(free_rooms)
        # push the end time of first meeting into heap 
        heapq.heappush(free_rooms,intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
        
            heapq.heappush(free_rooms,i[1])
        
        return len(free_rooms)

# Time: O(NlogN)
# Space:O(N)


