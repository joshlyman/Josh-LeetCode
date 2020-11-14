class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # first sort the height in desceding order
        # then insert each people in the location of K values 
        
        people.sort(key=lambda x:(-x[0],x[1]))
        output = []
        
        for p in people:
            output.insert(p[1],p)
        
        return output 

# Time: O(N^2), sort takes O(NlogN), then each insert takes O(K)time, so totally O(N^2)
# https://leetcode.com/problems/queue-reconstruction-by-height/solution/

# Space:O(N)