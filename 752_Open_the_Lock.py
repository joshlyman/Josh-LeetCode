# BFS 
# We can think of this problem as a shortest path problem on a graph: 
# there are 10000 nodes (strings '0000' to '9999'), and there is an edge between 
# two nodes if they differ in one digit, that digit differs by 1 (wrapping around, 
# 	so '0' and '9' differ by 1), and if both nodes are not in deadends.


# Shortest path finding, when the weights are constant, as in this case = 1, BFS is the best way to go.
# Best way to avoid TLE is by using deque and popleft() .
# [Using list() and pop(0) is a linear operation in Python, resulting in TLE]

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS: find the shortest path  
        # iterate queue to find the final node, return the depth
        
        def neighbours(node):
            neis = []
            for i in range(4):
                x = int(node[i])
                for d in [-1,1]:
                    # from x move to y by adding 1 or -1 
                    y = (x+d)%10
                    newnode = node[:i]+str(y)+node[i+1:]
                    
                    neis.append(newnode)
            return neis 
        
        # must remember how to write the deque including the ()
        queue = collections. deque([('0000',0)])
        
        # can also use dict instead of set here 
        visited = set(deadends)
        dead = set(deadends)
        
        while queue:
            node, depth = queue.popleft()
            
            if node == target:
                return depth 
            
            if node in dead:
                continue 
            
            for nei in neighbours(node):
                if nei in visited:
                    continue 
                
                # set use add function 
                visited.add(nei)
                queue.append((nei,depth+1))
        
        return -1 
        
# Time: O(N^2 *A^N + D), where A is the number of digits in our alphabet, 
# N is the number of digits in the lock, and D is the size of deadends. 
# We might visit every lock combination, plus we need to instantiate our set dead. 
# When we visit every lock combination, we spend O(N^2)time enumerating through and constructing each node.

# Space:O(A^N +D), for the queue and the set dead.          
                

# Other solution:

 def openLock(self, deadends, target):
        marker, depth = 'x', -1
        visited, q = set(deadends), deque(['0000'])

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                if node == target: 
                	return depth
                if node in visited: 
                	continue
                visited.add(node)
                q.extend(self.successors(node))
        
        return -1

    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res

