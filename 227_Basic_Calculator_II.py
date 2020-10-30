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