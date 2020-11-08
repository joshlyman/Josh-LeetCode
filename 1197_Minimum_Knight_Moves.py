# Main idea is to use BFS because it can find the shortest path from source to target 

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque()
        q.append([0,0,0])
        visited = set()
        visited.add((0,0))
        while q:
            r,c,steps = q.popleft()
            if r==x and c==y:
                return steps
            dirs = [(r-1,c-2),(r-2,c-1),(r-2,c+1),(r-1,c+2),(r+1,c-2),(r+2,c-1),(r+1,c+2),(r+2,c+1)]
            for i,j in dirs:
                if (i,j) not in visited:
                    q.append([i,j,steps+1])
                    visited.add((i,j))
        return -1

# Time: O(R+C)
# Space:O(R+C)

# V2

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        diffs = [(2,1), (1,2), (2, -1), (-1, 2), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        root = (0, 0)
        desired = (x,y)
        q = deque([(root, 0)])
        visited = set(root)
        while True:
            coords, dist = q.popleft()
            if coords == desired:
                return dist
            for nbr in self.getNeighbors(coords, diffs):
                if nbr not in visited:
                    q.append((nbr, dist+1))
                    visited.add(nbr)
        
    def getNeighbors(self, coords, diffs):
        return [(coords[0] + a, coords[1] + b) for (a,b) in diffs]

# Great, this looks simple. We've got 8 coordinates that we can move to in any given location. As with normal bfs, we build a queue, 
# keep track of what we've visited, and explore our 8 neighbors. Here's the catch, we get the dreaded TLE.

# So why? Well observe that our movements are completely symmetric. Whether our desination was (x,y), (x,-y), (-x,y), or (-x,-y), 
# our answer would be the exact same. So what we can do is restrict our search space to just one quadrant (namely the 1st 
# quadrant where x,y are both positive). Armed with this info, we make 2 tiny adjustments.

# Turn our "desired" destination from (x,y) -> (abs(x) abs(y)).

# When exploring our neighbors, if we ever fall outside of quadrant 1, ignore that neighbor. While we'd be tempted 
# to write something like nbr[0] >=0 and nbr[1] >=0, this is not quite right. This is because we'd be resitricting 
# some of the places we can get to. We need to leave a small buffer that gives the knight wiggle room of 1 extra step. 
# So we use nbr[0] >=-2 and nbr[1] >=-2.
# And voila, we get a working solution:

# optimization by only exploring one quadrant. 
class Solution(object):
    def minKnightMoves(self, x, y):
        diffs = [(2,1), (1,2), (2, -1), (-1, 2), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        root = (0, 0)

        # only explore 1st quadrant 
        desired = (abs(x),abs(y))
        q = collections.deque([(root, 0)])
        visited = set(root)
        while True:
            coords, dist = q.popleft()
            if coords == desired:
                return dist
            for nbr in self.getNeighbors(coords, diffs):

                # even if in 1st quadrant, we cannot use nbr[0] >=0 and nbr[1] >=0, need to leave some buff here, 
                # so we use nbr[0] >=-2 and nbr[1] >=-2 to 
                if nbr not in visited and nbr[0] >=-2 and nbr[1] >=-2:
                    q.append((nbr, dist+1))
                    visited.add(nbr)
        
    def getNeighbors(self, coords, diffs):
        return [(coords[0] + a, coords[1] + b) for (a,b) in diffs]