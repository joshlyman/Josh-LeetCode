# Explanation：
# https://leetcode.com/problems/mirror-reflection/discuss/313520/most-detailed-explanation-rather-than-code-of-course-including-code

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while (p * k % q != 0):
            k += 1
        if k % 2 == 0:
            return 0
        if (p* k / q) % 2 == 0:
            return 2
        if (p * k / q) % 2 == 1:
            return 1

# Time: O(logP)
# Space:O(1)