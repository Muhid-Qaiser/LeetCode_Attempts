class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0:
                if stack[-1] == "(" and c == ")" or stack[-1] == "[" and c == "]" or stack[-1] == "{" and c == "}":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if stack != [] :
            return False
        return True