class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True

# Time: O(NlogN)
# Space:O(N)


# Bucket Sort 

# trips.length <= 1000
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

# Time: O(max(N,1001))
# Space:O(1001) = O(1)