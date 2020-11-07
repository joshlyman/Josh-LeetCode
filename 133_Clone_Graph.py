"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS

class Solution:
    
    def __init__(self):
         # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]
        
        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])
        
        # The key is original node and value being the clone node.
        self.visited[node] = clone_node
        
        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node

# Time: O(N+M), where N is a number of nodes (vertices) and M is a number of edges.

# Space:O(N), This space is occupied by the visited hash map and in addition to that, space would also be occupied 
# by the recursion stack since we are adopting a recursive approach here. The space occupied by the recursion stack 
# would be equal to O(H) where H is the height of the graph. Overall, the space complexity would be O(N).


# BFS

# The difference is only in the traversal of DFS and BFS. As the name says it all, DFS explores the depths of the graph 
# first and BFS explores the breadth. Based on the kind of graph we are expecting we can chose one over the other. 
# We would need the visited hash map in both the approaches to avoid cycles.


# We will use a hash map to store the reference of the copy of all the nodes that have already been visited and copied. The key for the hash map would be the node of the original graph and corresponding value would be the corresponding cloned node of the cloned graph. The visited is used to prevent cycles and get the cloned copy of a node.

# Add the first node to the queue. Clone the first node and add it to visited hash map.

# Do the BFS traversal.

# Pop a node from the front of the queue.
# Visit all the neighbors of this node.
# If any of the neighbors was already visited then it must be present in the visited dictionary. Get the clone of this neighbor from visited in that case.
# Otherwise, create a clone and store in the visited.
# Add the clones of the neighbors to the corresponding list of the clone node.



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]

# Time: O(M+N)

# Space:O(N), This space is occupied by the visited dictionary and in addition to that, space would also be 
# occupied by the queue since we are adopting the BFS approach here. The space occupied by the queue would be 
# equal to O(W) where WW is the width of the graph. Overall, the space complexity would be O(N).











