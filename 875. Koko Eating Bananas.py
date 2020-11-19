class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(i/m) for i in piles])
            if time > H:
                l = m + 1
            else:
                r = m
        return l

Time: O(NlogW), where N is the number of piles, and W is the maximum size of a pile.
Space:O(1)