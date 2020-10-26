class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        res = []
        
        def backtrack(combination,next_digits):
            # if there is no more digits to check, then combination is done 
            if len(next_digits) ==0:
                res.append(combination)
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter,next_digits[1:])
       
        if digits:
            backtrack("",digits)
        return res 
        
# Time: O(3^N x 4^M), where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and 
# M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.
# Space: O(3^N x 4^M) 

# or we can use three for loops here 
        
        
        