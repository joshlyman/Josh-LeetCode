# The only difference between these two problems lies in the third sub-order. When two nodes have the same <column, row> index, 
# in this problem we would further order them based on their values, 
# while in the problem of 314 we would order them based on the horizontal order 
# from left to right. To illustrate the difference, we show an example in the following graph on how two nodes of the same 
# <column, row> index should be ordered respectively in these two problems.


# BFS with global sorting 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []
        
        def bfs(root):
            queue = deque([(root,0,0)])
            while queue:
                node,row,column = queue.popleft()
                if node is not None:
                    node_list.append((column,row,node.val))
                    queue.append((node.left,row+1,column-1))
                    queue.append((node.right,row+1,column+1))
        
        # step 1). construct the global node list, with the coordinates
        bfs(root)
        
        # step 2). sort the global node list, according to the coordinates and if same coords for multiple nodes, then sort based on value 
        node_list.sort()
        
        # # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for col,row,value in node_list:
            if col in ret:
                ret[col].append(value)
            else:
                ret[col] = [value]
        
        return ret.values()
    
  


# DFS with global sorting 
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        for column, row, value in node_list:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret

# Time: O(NlogN)

# In the first step of the algorithm, we traverse the input tree with either BFS or DFS, which would take O(N) time.
# Secondly, we sort the obtained list of coordinates which contains NN elements. The sorting operation would take O(NlogN) time.
# Finally, we extract the results from the sorted list, which would take another O(N) time.
# To summarize, the overall time complexity of the algorithm would be O(NlogN), which is dominated by the sorting operation in the second step.


# Space:O(N)   

# In the first step of the algorithm, we build a list that contains the coordinates of all the nodes. Hence, we need O(N) space for this list.
# Additionally, for the BFS approach, we used a queue data structure to maintain the order of visits. At any given moment, the queue contains no more than two levels of nodes in the tree. 
# The maximal number of nodes at one level is N/2, which is the number of the leaf nodes in a balanced binary tree. As a result, the space needed for the queue would be O(N/2)*2=O(N).
# Although we don't need the queue data structure for the DFS approach, the recursion in the DFS approach incurs some additional memory consumption on the function call stack. In the worst case, 
# the input tree might be completely imbalanced, e.g. each node has only the left child node. In this case, the recursion would occur up to N times, which in turn would consume O(N) space in the function call stack.
# To summarize, the space complexity for the BFS approach would be O(N). And the same applies to the DFS approach.

# Approach 2: BFS/DFS with Partition Sorting

# As we can see in the above approaches, the overall time complexity is dominated by the sorting operation on the list of coordinates. In order to further optimize the solution, we can try to do something with the sorting.
# It would be hard, if not impossible, to eliminate the sorting operation, since we still need a means to resolve the draw situation when two nodes share the same <column, row> index.
# One might argue that we could use the heap data structure (also known as PriorityQueue in Java) to maintain the list of coordinates. The elements in the heap data structure are ordered automatically, and this does eliminate the sorting operation. However, to maintain the elements in order, each insertion operation in heap would take \mathcal{O}(\log N)O(logN) time complexity. In other words, one can consider the heap data structure as another form of sorting, which amortizes the cost of sorting operating over each insertion.
# One could apply the head data structure to replace the sorting operation here, which could make the code more concise. But this is not the main point here.
# That being said, one thing that we can do is to reduce the scope of sorting, by partitioning the list of coordinates into subgroups based on the column index.

# BFS with sorting on subgroups by column 
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret

# DFS with sorting on subgroups by column 
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). DFS traversal
        DFS(root, 0, 0)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret

# Time: O(Nlog(N/K))

# In the first step, it takes O(N) time complexity for both the BFS and DFS traversal.

# In the second step, we need to sort the hashmap entry by entry. As we shown in the intuition section, the time complexity of sorting k equal-sized subgroups of 
# with total N elements would be O(k*(N/k)*log(N/k)) = O(Nlog(N/k))

# If we assume that the nodes are evenly aligned in the columns, then this would be the time complexity of sorting the obtained hashmap.
# 
# Finally, it takes another O(N) time complexity to extract the results from the hashmap.
# 
# As a result, the overall time complexity is O(Nlog(N/K))
# Although the sorting operation in the second step still dominates, it is more optimized compared to the previous approach of sorting the entire coordinates. 
# Let us look at one particular example. In the case where the tree is complete imbalanced (e.g. a node has only left node), 
# the tree would be partitioned into exactly N groups. Each group contains a single element. It would take no time to sort each group. As a result, 
# the overall time complexity of this approach becomes N*O(1)=O(N). While for the previous approach, its overall time complexity remains O(NlogN).

# Space:O(N)






