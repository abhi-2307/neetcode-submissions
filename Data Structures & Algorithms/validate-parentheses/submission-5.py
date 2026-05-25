class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        i = 0

        while i < len(s):

            if stack and (
                (s[i] == "}" and stack[-1] == "{") or
                (s[i] == ")" and stack[-1] == "(") or
                (s[i] == "]" and stack[-1] == "[")
            ):
                stack.pop()

            else:
                stack.append(s[i])

            i += 1

        return stack == []