# Refer from:
# https://leetcode.com/problems/alien-dictionary/solution/

# Topological sorting
# https://zh.wikipedia.org/wiki/%E6%8B%93%E6%92%B2%E6%8E%92%E5%BA%8F

# Where two words are adjacent, we need to look for the first difference between them. That difference tells us the relative order between two letters.

# All approaches break the problem into three steps:

# 1.Extracting dependency rules from the input. For example "A must be before C", "X must be before D", or "E must be before B".
# 2.Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
# 3. Topologically sorting the graph nodes.


# BFS 

# four of the letters have no arrows going into them. What this means is that there are no letters that have to be before any of these 
# four (remember that the question states there could be multiple valid orderings, and if there are, 
# then it's fine for us to return any of them). Put them in the list 

# then remove them and find next letters with no arrows going into them. Put them in the list 

# Then, instead of removing an edge from a reverse adjacency list, we can simply decrement the count by 1. 
# Once the count reaches 0, this is equivalent to there being no incoming edges left in the reverse adjacency list.

# We'll do a BFS for all letters that are reachable, adding each letter to the output as soon as it's reachable. 
# A letter is reachable once all of the letters that need to be before it have been added to the output. 
# To do a BFS, recall that we use a queue. We should initially put all letters with an in-degree of 0 onto that queue. 
# Each time a letter gets down to an in-degree of 0, it is added to the queue.

# We continue this until the queue is empty. After that, we check whether or not all letters were put in the output list. 
# If some are missing, this is because we got to a point where all remaining letters had at least one edge going in; 
# this means there must be a cycle! In that case, we should return "" as per the problem description. 
# Otherwise, we should return the complete ordering we found.

# One edge case we need to be careful of is where a word is followed by its own prefix. In these cases, 
# it is impossible to come up with a valid ordering and so we should return "". The best place to detect it is in 
# the loop that compares each adjacent pair of words.

# Also, remember that not all letters will necessarily have an edge going into or out of them. 
# These letters can go anywhere in the output. But we need to be careful to not forget 
# about them in our implementation.


from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


# Refer: https://leetcode.com/problems/alien-dictionary/solution/

# Time: O(C)
# Let N be the total number of strings in the input list.
# Let C be the total length of all the words in the input list, added together.
# Let U be the total number of unique letters in the alien alphabet. While this is limited to 
# 26 in the question description, we'll still look at how it would impact the complexity if it was not 
# limited (as this could potentially be a follow-up question).

# Space:O(1)O(1) or O(U+min(U^2,N)) 


# DFS
# Another approach to the third part is to use a depth-first search. We still need to extract relations and 
# then generate an adjacency list in the same way as before, but this time we don't need the indegrees map.

# Recall that in a depth-first search, nodes are returned once they either have no outgoing links left, 
# or all their outgoing links have been visited. Therefore, the order in which nodes are returned by 
# the depth-first search will be the reverse of a valid alphabet order.

# If we made a reverse adjacency list instead of a forward one, the output order would be correct (without needing to be reversed). 
# Remember that when we reverse the edges of a directed graph, the nodes with no incoming edges became the ones 
# with no outgoing edges. This means that the ones at the start of the alphabet will now be the ones returned first.

# One issue we need to be careful of is cycles. In directed graphs, we often detect cycles by using graph coloring. 
# All nodes start as white, and then once they're first visited they become grey, and then once all their outgoing 
# nodes have been fully explored, they become black. We know there is a cycle if we enter a node that is 
# currently grey (it works because all nodes that are currently on the stack are grey. Nodes are changed to 
# 	black when they are removed from the stack).

# Diff between BFS and DFS
# https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/

# The Time complexity of BFS is O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.

# The Time complexity of DFS is also O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.

# from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""

        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)

# Time: O(C)
# Space:O(1)O(1) or O(U+min(U^2,N)) 


# Other solutions:
# https://leetcode.com/problems/alien-dictionary/discuss/70281/Python-topological-sort-wo-BFSGFS

# We do not need a DFS or BFS to detect if there is a cycle, because if the graph stop shrinking before all nodes are removed, 
# it indicates that solution doesn't exist (a cycle in the graph)

class Node(object):
	def __init__(self):
	    self.IN = set()
	    self.OUT = set()

class Solution(object):
	def alienOrder(self, words):
	   # find out nodes
	   graph = {}
	    for word in words:
	        for letter in word:
	            if letter not in graph:
	                graph[letter] = Node()

	    # find out directed edges (from StefanPochmann)
	    for pair in zip(words, words[1:]):
	        for a, b in zip(*pair):
	            if a != b:
	                graph[a].OUT.add(b)
	                graph[b].IN.add(a)
	                break

	    # topo-sort
	    res = ""
	    while graph:
	        oldlen = len(graph)

	        for key in graph:
	            if not graph[key].IN:   # to remove this
	                for key2 in graph[key].OUT:
	                    graph[key2].IN.remove(key)
	                del graph[key]
	                res += key
	                break

	        if oldlen == len(graph): # if shrinking stops, solution doesn't exist
	            return ""
	        oldlen = len(graph)
	    return res


# https://leetcode.com/problems/alien-dictionary/discuss/70239/Simple-Python-solution-best-runtime
from collections import deque

class Solution(object):
    def alienOrder(self, words):
        chars = set(c for w in words for c in w)
        graph, indeg = {c:[] for c in chars}, {c:0 for c in chars}
        for pair in zip(words, words[1:]):
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    graph[c1] += c2,
                    indeg[c2] += 1
                    break

        queue = deque([char 
                       for char in indeg 
                       if not indeg[char]])
        ret = ""
        while queue:
            char = queue.popleft()
            ret += char
            for n in graph[char]:
                indeg[n] -= 1
                if not indeg[n]:
                    queue.append(n)
        return ret * (set(ret) == chars)







# 


