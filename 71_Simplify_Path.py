class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for comp in path:
            if comp == "" or comp == ".":
                continue
            elif comp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        
        return '/' + "/".join(stack)

        