class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openChars = "({["
        for c in s:
            if c in openChars:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack
