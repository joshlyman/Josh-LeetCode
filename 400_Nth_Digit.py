# Refer from:
# https://leetcode.com/problems/nth-digit/discuss/88363/Java-solution

# 1.find the length of the number where the nth digit is from
# 2.find the actual number where the nth digit is from
# 3.find the nth digit and return

# Use Java
public int findNthDigit(int n) {
		int len = 1;
		long count = 9;
		int start = 1;

		while (n > len * count) {
			n -= len * count;
			len += 1;
			count *= 10;
			start *= 10;
		}

		start += (n - 1) / len;
		String s = Integer.toString(start);
		return Character.getNumericValue(s.charAt((n - 1) % len));
	}

# Refer from:
# https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis 

class Solution(object):
    def findNthDigit(self, n):
        start, size = 1, 1
        while n > size:
            n, start = n - size, start + 1
            size = len(str(start))
        return int(str(start)[n-1])

# Time: O(N)
# Space:O(1)



class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])

# Time: O(logN)
# Space:O(1)

# The while loop takes O(log(n)) time because a number n will have at most O(log(n)) digits. 
# Then the return statement takes O(log(n)) time to convert the number to string. So total time complexity 
# is O(log(n)), with O(log(n)) extra space for the string.


# My solution:

class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1
        size = 1
        count = 9
        
        # find where the nth digit is from by decreasing n
        while n > size*count:
            n -= size*count 
            size +=1
            count *=10
            start *=10
        
        # get the target number 
        # current n is the number that falls in the range 
        start +=(n-1)//size 
        strNum = str(start)
        
        # get nth digit 
        ndigit = int(strNum[(n-1)%size])
        
        return ndigit

# Time: O(logN)
# Space:O(1)
