class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
    
        for i in range(len(s)):

            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            
            if s[i] in '+-*/' or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    p = stack.pop()
                    
                    # cannot pass neg number, for example:
                    # -3//2 = -2, not -1
                    res = abs(p) // num
                    stack.append(res if p >= 0 else -res)
                    # res = p//num
                    # stack.append(res)
                num = 0
                sign = s[i]

        return sum(stack)

# Time: O(N)
# Space:O(N)


# V2: same template with 224 I and 722 III
class Solution:
    def calculate(self, s: str) -> int:
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c 
            return sum(stack)
        return helper([], 0)
