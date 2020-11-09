# Moving window 

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []
        
    def next(self, val: int) -> float:
        size = self.size
        queue = self.queue
        queue.append(val)
        
        # sum last size of value 
        window_sum = sum(queue[-size:])
        
        # maybe length of queue will be smaller than size 
        return window_sum / min(len(queue), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Time: O(N), N is the size of moving window
# Space:O(M), where M is the length of the queue which would grow at each invocation of the next(val) function.


# use Deque to save time and space

# Deques are a generalization of stacks and queues (the name is pronounced deck and is 
# short for double-ended queue). Deques support thread-safe, memory efficient appends 
# and pops from either side of the deque with approximately the same O(1) performance 
# in either direction.

from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)

# Time: O(1)
# Space:O(N), where N is the size of the moving window.

