class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # 1.linear search to check the row with very first 1st then return the column
        # too many calls fail 


        # Time: O(NM), N is no. of rows and M is no. of columns 
        # Space:O(1)


        # 2.Binary search each row 
		rows,cols = binaryMatrix.dimensions()
        smallest_index = cols 
        
        for row in range(rows):
            
            lo = 0
            hi = cols -1 
            
            while lo < hi:
                mid = (lo+hi)//2
                
                if binaryMatrix.get(row,mid) ==0:
                    lo = mid+1
                else:
                    hi = mid 
            
            # only check left pointer as column index 
            if binaryMatrix.get(row,lo) == 1:
                smallest_index = min(smallest_index,lo)
        
        # if does not found, then return -1
        if smallest_index == cols:
            return -1
        else:
            return smallest_index


  		# Time: O(NlogM)
  		# Space:O(1)


  		 # 3.start from top right, move only left and down 
 class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        rows, cols = binaryMatrix.dimensions()
        
        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols -1
        
        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >=0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1
        
        # If we never left the last column, it must have been all 0's.
        if current_col == cols -1:
            return -1 
        else:
            return current_col + 1 


        # Time: O(N+M)
  		# Space:O(1)

