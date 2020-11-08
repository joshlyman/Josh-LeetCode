# The trick is to count the elements of T. After we have some count[char] = 
# (the number of occurrences of char in T), we can write these elements in the order we want. 
# The order is S + (characters not in S in any order).


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = collections.Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)
        
# Time: O(S.length+T.length)
# Space:O(T.length)