# what is a graph bipartite?
# https://www.youtube.com/watch?v=670Gn4e89B8&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90


# We should be careful to consider disconnected components of the graph, by searching each node. 
# For each uncolored node, we'll start the coloring process by doing a depth-first-search on that 
# node. Every neighbor gets colored the opposite color from the current node. If we find a neighbor 
# colored the same color as the current node, then our coloring was impossible.

# To perform the depth-first search, we use a stack. For each uncolored neighbor in graph[node], 
# we'll color it and add it to our stack, which acts as a sort of "todo list" of nodes to visit next. 
# Our larger loop for start... ensures that we color every node.

# DFS with iterative 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for neighb in graph[node]:
                        if neighb not in color:
                            # do DFS to put neigb node in stack 
                            stack.append(neighb)
                            color[neighb] = 1-color[node]
                            # color[nei] = color[node] ^ 1
                        elif color[neighb] == color[node]:
                            return False
        
        return True 

# Time: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. 
# We explore each node once when we transform it from uncolored to colored, 
# traversing all its edges in the process.

# Space:O(N), the space used to store the color.

# BFS with iterative  
 class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque 
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = deque()
                queue.append(node)
                
                color[node] = 0
                while queue:
                    node = queue.popleft()
                    for neighb in graph[node]:
                        if neighb not in color:
                            # do DFS to put neigb node in stack 
                            queue.append(neighb)
                            color[neighb] = 1-color[node]
                            # color[nei] = color[node] ^ 1
                        elif color[neighb] == color[node]:
                            return False
        
        return True 

# Time: O(N+E)
# Space:O(N)

# Other solutions:
# https://leetcode.com/problems/is-graph-bipartite/discuss/480343/Python-2-DFS-%2B-2-BFS

