
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = collections.deque([])
        stack.append(s[0])

        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] != s[i] and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])

        return len(stack)

