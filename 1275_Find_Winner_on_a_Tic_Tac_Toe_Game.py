# Refer from:
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/discuss/731461/Python-Short-Optimized-and-Interview-Friendly-Solution

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        n = 3
        rows = [0]*n
        cols = [0]*n
        
        # y = x
        diag1 = 0
        # y = -x
        diag2 = 0
        
        for index,move in enumerate(moves):
            
            i,j = move[0],move[1]
            
            # sign 1 is A, -1 is B 
            if index%2 == 0:
                sign = 1
            else:
                sign = -1
            
            rows[i] += sign
            cols[j] += sign
            
            # y = x
            if i == j:
                diag1 +=sign
            
            # y = -x
            if i+j == n-1:
                diag2 +=sign
            
            # once satisfy condition, game will stop  
            if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag1) == n or abs(diag2) == n:
                if sign == 1:
                    return "A"
                else:
                    return "B"
        if len(moves) == n*n:
            return "Draw"
        else:
            return "Pending"
                
 # Time: O(N)
 # Space:O(N)          
            
            
            
            
            

