class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        
        # maintain a min heap which contains only k elements, so kth element will be the smallest element, which is kth largest element 
        while len(self.pool) > k:
            heapq.heappop(self.pool)

        
    def add(self, val):
        if len(self.pool) < self.k:
            # push item on the heap 
            heapq.heappush(self.pool, val)
        else:
            # Push item on the heap, then pop and return the smallest item from the heap.
            heapq.heappushpop(self.pool, val)
        
        # 1st one is the top one, smallest one in min heap 
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# In initialization:
# Time: O(logN)
# Space:O(N)

# In add:
# Time: O(logK) +O(1)
# Space:O(K)

# Heapfication is O(log n) time and O(n) space 

# during initialization it appears to be O(log N) time and O(K) space, 
# but for add, it's O(log K) + O(1) time and O(k) space as the heap size 
# is constrained to K (NOT N where N is the input nums). The O(1) comes 
# from having to read from the top of the heap to return the value which is constant-time.