class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        sum = 0
        for i in range(len(ops)):
            if ops[i]=="C":
                sum-=stack[-1]
                stack.pop()
            elif ops[i]=="+":
                sum+=(stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif ops[i]=='D':
                sum+=stack[-1]*2
                stack.append(2*stack[-1])
            else:
                stack.append(int(ops[i]))
                sum+=int(ops[i])
        return sum
        