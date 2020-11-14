# BFS
# https://leetcode.com/problems/the-maze/discuss/198453/Python-BFS-tm

class Solution:
    from collections import deque 
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # up down left right
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        visited[start[0]][start[1]] = True

        q = deque([start])

        while q:
            tup = q.popleft()
            if tup[0] == destination[0] and tup[1] == destination[1]:
                return True

            for dir in dirs:
                # Roll the ball until it hits a wall
                row = tup[0] + dir[0]
                col = tup[1] + dir[1]

                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
                    row += dir[0]
                    col += dir[1]

                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                (new_x, new_y) = (row - dir[0], col - dir[1])

                # Check if the new starting position has been visited
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return False

# Time: O(MN)
# Space:O(MN)

# DFS

class Solution:
    def hasPath(self, maze, start, destination):
        m, n, stopped = len(maze), len(maze[0]), set()
        def dfs(x, y):
            if (x, y) in stopped: 
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True
            return False
        return dfs(*start)

# Time: O(MN)
# Space:O(MN)     