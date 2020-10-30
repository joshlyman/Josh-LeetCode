Different with 157 called once, if called multiple times, then

https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/49601/What-is-the-difference-between-call-once-and-call-multiple-times 

Think that you have 4 chars "a, b, c, d" in the file, and you want to call your function twice like this:

read(buf, 1); // should return 'a'
read(buf, 3); // should return 'b, c, d'
All the 4 chars will be consumed in the first call. So the tricky part of this question is how can you preserve the remaining 'b, c, d' to the second call.



So we need queue to store the previous called numbers and pop up when calling again 

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n-idx)
            for i in range(curr):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if curr == 0:
                break 
        return idx

# Time: O(N)
# Space:O(N)