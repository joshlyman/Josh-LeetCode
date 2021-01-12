class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in range(len(ops)):
            op = ops[i]
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)

# Time: O(N)
# Space:O(N)