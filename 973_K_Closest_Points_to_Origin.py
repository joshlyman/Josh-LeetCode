# Details: 
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/885664/Python-Four-solutions%3A-Sort-Minheap-Maxheap-Quickselect 

# 1.sort based on a key function (distance) then return the k closet points 
# this will take N(logN) time for sorting
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 1.sort based on a key function (distance) then return the k closet points 
        # this will take N(logN) time for sorting
        
        points.sort(key=lambda p:p[0]**2+p[1]**2)
        return points[0:K]        

# Time: (NlogN)
# Space:(N)


# 2.Min Heap 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapq.heapify(arr)
        res = []
        for _ in range(K):
            res.append(heapq.heappop(arr)[1])
        return res       

# Time: (N+KlogN), K is size of heap 
# Space:(N)



# 3. Max Heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = [(-1 * (p[0] ** 2 + p[1] ** 2), p) for p in points]
        heap = arr[:K]
        heapq.heapify(heap)
        for p in arr[K:]:
            heapq.heappushpop(heap, p)
        return [coord for distance, coord in heap]

# Time: (NlogK), K is size of heap 
# Space:(K)


# 4. Quickselect (Divide and Conquer) 
# refer from https://github.com/deepti-talesra/LeetCode/blob/master/K_Closest_Points_to_Origin.py
# https://www.youtube.com/watch?v=3OxgmzezTG8&ab_channel=DEEPTITALESRA

# other version:
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/220326/Python3-Solution-using-QuickSelect-O(NlogN)
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/885664/Python-Four-solutions%3A-Sort-Minheap-Maxheap-Quickselect 

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    import random 
    lst = [(i, self.dist(i)) for i in points]
    return self.find(lst, K)
        
def dist(self, pt):
    return pt[0] ** 2 + pt[1] ** 2
 
  
def find(self, lst, K):
    if len(lst) == K:
        return [i[0] for i in lst]

    rand_tup = random.choice(lst)
    pivot = rand_tup[1]

    i = 0
    left = []
    right = []
    equal = []

    while i < len(lst):
        curr = lst[i]
        dist = curr[1]
        if dist < pivot:
            left.append(curr)
        elif dist == pivot:
            equal.append(curr)
        else:
            right.append(curr)
        i += 1
    len_left = len(left)
    if len_left == K:
        return [i[0] for i in left]
    if len_left + len(equal) == K:
        return [i[0] for i in left] + [i[0] for i in equal]
    if K < len_left:
        return self.find(left, K)
    else:
        return [i[0] for i in left] + [i[0] for i in equal] + self.find(right, K - len_left - len(equal)) 

# Time: average and best case is O(n), worst case is O(n^2), K is size of heap 
# Space:(n)










