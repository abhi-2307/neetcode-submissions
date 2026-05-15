class Solution:
    def isValid(self, s: str) -> bool:
        open = ["{", "(", "["]
        stack = []
        i=0
        while i < len(s):
            if s[i] in open:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (s[i]=="}" and stack[-1] == "{") or (s[i]==")" and stack[-1] == "(") or (s[i]=="]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
            i+=1
        return stack==[]
