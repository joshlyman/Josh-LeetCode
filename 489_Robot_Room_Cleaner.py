# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# DFS
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        # initial direction is move up 
        self.dfs(robot, 0, 0, 0, 1, set())
    
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        # clean current cell
        robot.clean()

        # store visited cell 
        visited.add((x, y))
        
        for k in range(4):

            # traversal all neighbors 
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y

            # if move up without obstacle, then go 
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                
                # back to previous location and direction 
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            # change direction in anticlockwise each time, so turn left because default is to move directly: robot.move()
            robot.turnLeft()

            # change direction in anticlockwise : (0,1) becomes (-1,0), then (0,-1), then (1,0)
            direction_x, direction_y = -direction_y, direction_x 
        

# Time: O(N-M)
# Space:O(N-M)


# V2 DFS 
class Solution:
    def cleanRoom(self, robot):
        path = set()
        def dfs(x, y, dx, dy):
            # 1, Clean current
            robot.clean()
            path.add((x, y))

            # 2, Clean next
            for _ in range(4):
                if (x + dx, y + dy) not in path and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx

            # 3, Back to previous position and direction
            robot.turnLeft(); robot.turnLeft()
            robot.move()
            robot.turnLeft(); robot.turnLeft()

        dfs(0, 0, 0, 1)

# Backtracking 

# Mark the cell as visited and clean it up.

# Explore 4 directions : up, right, down, and left (the order is important since the idea is always to turn right) :

# Check the next cell in the chosen direction :

# If it's not visited yet and there is no obtacles :

# Move forward.

# Explore next cells backtrack(new_cell, new_direction).

# Backtrack, i.e. go back to the previous cell.

# Turn right because now there is an obstacle (or a virtual obstacle) just in front.


class Solution(object):       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])
                
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()
    
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()


# Time: O(N-M)
# Space:O(N-M)




