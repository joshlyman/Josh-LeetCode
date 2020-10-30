# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# DFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def DFS(nestedList, depth):
            temp_sum = 0
            
            for member in nestedList:
                if member.isInteger():
                    temp_sum += member.getInteger() * depth
                else:
                    temp_sum += DFS(member.getList(),depth+1)
            return temp_sum
        
        return DFS(nestedList,1)
        

Time: O(N)
Space:O(1)        


# BFS
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        queue = deque([(n_int, 1) for n_int in nestedList])
        while queue:
            n_int, depth = queue.popleft()
            if n_int.isInteger():
                res += n_int.getInteger() * depth
            else:
                for i in n_int.getList():
                    queue.append((i, depth + 1))
        return res

        

