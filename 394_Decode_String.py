class Solution:
    def decodeString(self, s: str) -> str:

        stack = []        

        for i in s:
            temp = []
            if i != ']':
                if stack and i.isdigit() and stack[-1].isdigit():
                    stack[-1] += i
                else:
                    stack.append(i)
            else:
                curr = stack.pop()
                while stack and curr != '[':
                    temp.insert(0, curr)
                    curr = stack.pop()
                n = stack.pop()
                temp = temp * int(n)
                stack.append( "".join(temp) )

        return "".join(stack)
        