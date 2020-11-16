# we can use max heap to do, time will be O(KlogK)


# Binary search will speed up in this case and we dont need to use heap to store it, just use two pointers 

# Assume A[mid] ~ A[mid + k] is sliding window
# case 1: x - A[mid] < A[mid + k] - x, need to move window go left
# -------x----A[mid]-----------------A[mid + k]----------

# case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
# -------A[mid]----x-----------------A[mid + k]----------

# case 3: x - A[mid] > A[mid + k] - x, need to move window go right
# -------A[mid]------------------x---A[mid + k]----------

# case 4: x - A[mid] > A[mid + k] - x, need to move window go right
# -------A[mid]---------------------A[mid + k]----x------


# If x - A[mid] > A[mid + k] - x,
# it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
# and we have mid smaller than the right i.
# So assign left = mid + 1.


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

# Time: O(log(N-K))
# Space:O(K)