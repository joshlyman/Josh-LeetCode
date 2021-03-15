
https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation


Let's see the relationship between the Excel sheet column title and the number:

A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)




class Solution:
    def convertToTitle(self, n: int) -> str:
        column = []
        while n > 0:
            
            # # number is the int part, output is 
            # number, output = divmod(number-1, 26)
            
            # number should start from 0, so number - 1, it means 0+'A' 
            div = (n-1)//26
            output = (n-1)%26
            n = div 
            
            # 28 will be: ['1','0'] so need to reverse later 
            column.append(output)
            
            
        # start from 'A' to transfer each number to chr 
        return ''.join([chr(i+ord('A')) for i in reversed(column)])

# Time: O(N)
# Space:O(N)

