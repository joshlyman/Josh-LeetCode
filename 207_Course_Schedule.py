# https://www.jiuzhang.com/problem/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # prerequisites = [[1,0]] 
        # 0 -> 1 
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] +=1
        
        num_choose = 0
        queue = collections.deque()
        
        # put the node with 0 indegree into queue 
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 0 has 0 indegree, 0:[1]
        while queue:
            now_pos = queue.popleft()
            num_choose +=1
            
            # delete each neighbour pos from in_degree, if indegree is 0, then add into queue 
            for next_pos in graph[now_pos]:
                # [1]: indegree from 1 to 0 
                in_degree[next_pos] -=1
                
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        
        return num_choose == numCourses



# refer from:
# https://leetcode.com/problems/course-schedule/solution/

# Approach 1: Backtracking

# The general idea here is that we could enumerate each course (vertex), to check if it could form cyclic dependencies (i.e. a cyclic path) starting from this course.

# The check of cyclic dependencies for each course could be done via backtracking, where we incrementally follow the dependencies until either there is no more dependency or we come across a previously visited course along the path.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import defaultdict 
        
        courseDict = defaultdict(list)
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            # prevCourse -> nextCourse
            courseDict[prevCourse].append(nextCourse)
            
        path = [False]*numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path):
                return False
        
        return True 
    
    def isCyclic(self,currCourse,courseDict,path):
        # backtracking or dfs to check that no cycle would be formed starting from currCourse
        if path[currCourse]:
             # come across a previously visited node, i.e. detect the cycle
            return True
        
        # before backtracking, mark the node in the path
        path[currCourse] = True
        
        # backtracking
        ret = False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, path)
            if ret: break 
        
        # after backtracking, remove the node from the path
        path[currCourse] = False
        return ret 
    
# Time: O(|E| +|V|) 
# Space:O(|E| +|V|) 
   
    
# Time: O(∣E∣+∣V∣^2), where ∣E∣ is the number of dependencies, ∣V∣ is the number of courses and dd is the maximum length of acyclic paths in the graph.

# First of all, it would take us ∣E∣ steps to build a graph in the first step.
# For a single round of backtracking, in the worst case where all the nodes chained up in a line, it would take us maximum ∣V∣ steps to terminate the backtracking.

# Again, follow the above worst scenario where all nodes are chained up in a line, it would take us in total sum(i to v) i = (1+|V|)*|V|/2
  # steps to finish the check for all nodes.

# Space Complexity: O(∣E∣+∣V∣), with the same denotation as in the above time complexity.

# Approach 2: Postorder DFS

# The rationale is that given a node, if the subgraph formed by all descendant nodes from this node has no cycle, then adding this node to the subgraph would not form a cycle either.

# Step 1). We build a graph data structure from the given list of course dependencies.
# Step 2). We then enumerate each node (course) in the constructed graph, to check if we could form a dependency cycle starting from the node.
# Step 3.1). We check if the current node has been checked before, otherwise we enumerate through its child nodes via backtracking, where we breadcrumb our path (i.e. mark the nodes we visited) to detect if we come across a previously visited node (hence a cycle detected). We also remove the breadcrumbs for each iteration.
# Step 3.2). Once we visited all the child nodes (i.e. postorder), we mark the current node as checked.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, checked, path):
        """   """
        # 1). bottom-cases
        if checked[currCourse]:
            # this node has been checked, no cycle would be formed with this node.
            return False
        if path[currCourse]:
            # came across a marked node in the path, cyclic !
            return True

        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[currCourse] = True

        ret = False
        # postorder DFS, to visit all its children first.
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break

        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False

        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret

# Time: O(|E| +|V|) 
# Space:O(|E| +|V|) 



# Approach 3: Toplogical Sort 

# Actually, the problem is also known as topological sort problem, which is to find a global 
# order for all nodes in a DAG (Directed Acyclic Graph) with regarding to their dependencies.


# L = Empty list that will contain the sorted elements
# S = Set of all nodes with no incoming edge

# while S is non-empty do
#     remove a node n from S
#     add n to tail of L
#     for each node m with an edge e from n to m do
#         remove edge e from the graph
#         if m has no other incoming edges then
#             insert m into S

# if graph has edges then
#     return error   (graph has at least one cycle)
# else 
#     return L   (a topologically sorted order)

# To better understand the above algorithm, we summarize a few points here:

# In order to find a global order, we can start from those nodes which do not have any prerequisites (i.e. indegree of node is zero), we then incrementally add new nodes to the global order, following the dependencies (edges).
# Once we follow an edge, we then remove it from the graph.
# With the removal of edges, there would more nodes appearing without any prerequisite dependency, in addition to the initial list in the first step.
# The algorithm would terminate when we can no longer remove edges from the graph. There are two possible outcomes:
# 1). If there are still some edges left in the graph, then these edges must have formed certain cycles, which is similar to the deadlock situation. It is due to these cyclic dependencies that we cannot remove them during the above processes.
# 2). Otherwise, i.e. we have removed all the edges from the graph, and we got ourselves a topological order of the graph.


class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False
            
# Time: O(|E| +|V|) 
# Space:O(|E| +|V|) 








