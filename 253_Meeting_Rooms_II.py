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

# Time: O(nlogn), sorting takes nlogn
# Space:O(1)

