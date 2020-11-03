
# Refer from:
# https://leetcode.com/problems/task-scheduler/solution/

# The total number of CPU intervals we need consists of busy and idle slots. Number of busy slots is defined by the number of tasks to execute: len(tasks). The problem is to compute a number of idle slots.

# Maximum possible number of idle slots is defined by the frequency of the most frequent task: 
# idle_time <= (f_max - 1) * n.

# This maximum could be decreased because one doesn't need to keep the CPU idle during cooling periods. It could execute different tasks as well.



# Approach 1: greedy 

# The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.

# Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.

# Sort the array and retrieve the maximum frequency f_max. This frequency defines the max possible idle time: idle_time = (f_max - 1) * n.

# Pick the elements in the descending order one by one. At each step, decrease the idle time by min(f_max - 1, f) where f is a current frequency. Remember, that idle_time is greater or equal to 0.

# Return busy slots + idle slots: len(tasks) + idle_time.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        
        for t in tasks:
            freq[ord(t) - ord('A')]+=1
        
        # here sorting is O(N), because 
        freq.sort()
        
        # max freq
        f_max = freq.pop()
        
        # # of idle time depends on the most freq number
        idle_time = (f_max - 1) * n
        
        while freq and idle_time >0:
            idle_time -= min(f_max-1,freq.pop())
        
        
        idle_time = max(0,idle_time)
        
        return idle_time + len(tasks)
        
        

# Time: O(Ntotal), N total is a number of tasks to execute. This time is needed to iterate over the input array tasks and 
# compute the array frequencies. Array frequencies contains 26 elements, and hence all operations 
# with it takes constant time. so sorting takes O(1) time 

# Space:O(1) 

# Approach 2: Math 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

 # Time: O(Ntotal)
 # Space:O(1)     







