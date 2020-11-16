# we can use BFS or DFS to iterative each node to build tree and find the height but this will take O(N^2) time 

# We need to use topological sorting 

# https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts


# First let's review some statement for tree in graph theory:

# (1) A tree is an undirected graph in which any two vertices are
# connected by exactly one path.

# (2) Any connected graph who has n nodes with n-1 edges is a tree.

# (3) The degree of a vertex of a graph is the number of
# edges incident to the vertex.

# (4) A leaf is a vertex of degree 1. An internal vertex is a vertex of
# degree at least 2.

# (5) A path graph is a tree with two or more vertices that is not
# branched at all.

# (6) A tree is called a rooted tree if one vertex has been designated
# the root.

# (7) The height of a rooted tree is the number of edges on the longest
# downward path between root and a leaf.

# OK. Let's stop here and look at our problem.

# Our problem want us to find the minimum height trees and return their root labels. First we can think about a simple case -- a path graph.

# For a path graph of n nodes, find the minimum height trees is trivial. Just designate the middle point(s) as roots.

# Despite its triviality, let design a algorithm to find them.

# Suppose we don't know n, nor do we have random access of the nodes. We have to traversal. It is very easy to get the idea of two pointers. One from each end and move at the same speed. When they meet or they are one step away, (depends on the parity of n), we have the roots we want.

# This gives us a lot of useful ideas to crack our real problem.

# For a tree we can do some thing similar. We start from every end, by end we mean vertex of degree 1 (aka leaves). We let the pointers move the same speed. When two pointers meet, we keep only one of them, until the last two pointers meet or one step away we then find the roots.

# It is easy to see that the last two pointers are from the two ends of the longest path in the graph.


# Topogical sorting 
# # The actual implementation is similar to the BFS topological sort. Remove the leaves, 
# update the degrees of inner vertexes. Then remove the new leaves. Doing so level by level until 
# there are 2 or 1 nodes left. What's left is our answer!

# The time complexity and space complexity are both O(n).

# Note that for a tree we always have V = n, E = n-1.






# approach

# Initially, we would build a graph with the adjacency list from the input.

# We then create a queue which would be used to hold the leaf nodes.

# At the beginning, we put all the current leaf nodes into the queue.

# We then run a loop until there is only two nodes left in the graph.

# At each iteration, we remove the current leaf nodes from the queue. While removing the nodes, 
# we also remove the edges that are linked to the nodes. As a consequence, some of the non-leaf nodes 
# would become leaf nodes. And these are the nodes that would be trimmed out in the next iteration.

# The iteration terminates when there are no more than two nodes left in the graph, 
# which are the desired centroids nodes.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0] 
        
        adj = [set() for _ in range(n)]
        
        # each node 
        # for ind in edges:
        #     adj[ind[0]].add(ind[1])
        #     adj[ind[1]].add(ind[0])
        
        # store each connected adj path into the list of sets
        # each set is a node and contains the nodes they connect to 
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        # get leaves if containing only 1 node 
        # in this case:[[1,0],[1,2],[1,3]], leaves are 0,2,3 
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        # loop from leaves until node number is less or equal than 2
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                # j: root or connected node, pop root from leave node  
                j = adj[i].pop()
                # i: leave node, from root's nodes remove this leave 
                # update degree of inner vertex 
                adj[j].remove(i)
                # after removing leave, some other nodes will become leave nodes 
                # we put them inside and continue removing 
                if len(adj[j]) == 1: 
                    newLeaves.append(j)
            
            # final remaining leaves are the roots
            leaves = newLeaves
        return leaves


# Time: O(|V|), V is # of nodes in the graph

# First, it takes |V|-1∣V∣−1 iterations for us to construct a graph, given the edges.

# With the constructed graph, we retrieve the initial leaf nodes, which takes |V|∣V∣ steps.

# During the BFS trimming process, we will trim out almost all the nodes (|V|∣V∣) and edges (|V|-1∣V∣−1) from the edges. Therefore, it would take us around |V| + |V| - 1∣V∣+∣V∣−1 operations to reach the centroids.

# To sum up, the overall time complexity of the algorithm is O(∣V∣).




# Space:O(|V|)

# We construct the graph with adjacency list, which has |V|∣V∣ nodes and |V|-1∣V∣−1 edges. Therefore, we would need |V| + |V|-1∣V∣+∣V∣−1 space for the representation of the graph.

# In addition, we use a queue to keep track of the leaf nodes. In the worst case, the nodes form a star shape, with one centroid and the rest of the nodes as leaf nodes. In this case, we would need |V|-1∣V∣−1 space for the queue.

# To sum up, the overall space complexity of the algorithm is also O(∣V∣).















