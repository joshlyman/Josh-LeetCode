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
        
        # different with permutations, need to add index to record the location, we dont want all combinations because order matters, index dont need to be recovered, we dont need to record used sets because based on index, not possible to reuse, so index can replace used, we need to recover index   
        # index, path, used, candidates, results
        index = 0
        path = []
        results = []
        
        if not digits:
            return []
        
        def dfs(index,path):
            if index == len(digits):
                results.append("".join(path))
                return 
                
            for letter in phone[digits[index]]:         
                path.append(letter)
                index +=1
                dfs(index,path)
                index -=1
                path.pop()
        
        dfs(index,path)                        
        return results                  
                              
            
                              
                        
        
# https://www.jiuzhang.com/problem/letter-combinations-of-a-phone-number/     
        
# Time: O(3^N x 4^M), where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and 
# M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.
# Space: O(3^N x 4^M) 

# or we can use three for loops here 
        
        
        