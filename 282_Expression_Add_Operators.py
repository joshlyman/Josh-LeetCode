# Refer from:
# https://leetcode.com/problems/expression-add-operators/solution/

# offical solution
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return answers

# Time: O(Nx4^N)
# Space:O(N)


# Other solution:
# https://leetcode.com/problems/expression-add-operators/discuss/71968/Clean-Python-DFS-with-comments

# dfs() parameters:
# num: remaining num string
# temp: temporally string with operators added
# cur: current result of "temp" string
# last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
# res: result to return

# DFS + recursion 
def addOperators(self, num, target):
    res, self.target = [], target
    for i in range(1,len(num)+1):
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
    return res

def dfs(self, num, temp, cur, last, res):
    if not num:
        if cur == self.target:
            res.append(temp)
        return
    for i in range(1, len(num)+1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
            self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
            self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)

# Time: O(3^N)
# Space:O(N)


# Easy to understand!

# Other solution
# https://leetcode.com/problems/expression-add-operators/discuss/385450/Python-solution-320ms-18-lines-with-easy-to-understand-variable-names-and-explanation

def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []
        res = []

        def helper(start, expr, val, prev):
            if val == target and start == len(num):
                res.append(expr); return
            if start < len(num) and max(1, abs(prev)) * (int(num[start:])) < abs(target - val): return   # target not reachable
            for i in range(start, len(num)):
                curr = num[start: i+1]
                if len(curr) != len(str(int(curr))): break   # prevent '00','01',... treated as one number
                if start == 0:
                    helper(i+1, curr, int(curr), int(curr))
                else:
                    helper(i+1, expr+'+'+curr, val+int(curr), int(curr))
                    helper(i+1, expr+'-'+curr, val-int(curr), -int(curr))   # -curr is interpreted as +(-curr)
                    helper(i+1, expr+'*'+curr, val-prev+prev*int(curr), prev*int(curr))   # since * has precedence over + we have to roll back +prev
        
        helper(0, '', 0, 0)
        return res




