class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for idx, c in enumerate(s):
            if c == "(":
                stack.append((0, idx))
            elif c == ")":
                if stack and stack[-1][0] == 0:
                    stack.pop()
                else:
                    stack.append((1, idx))
        start_idx, ans = 0, ""

        for end in stack:
            ans += s[start_idx:end[1]]
            start_idx = end[1] + 1

        ans += s[start_idx:]

        return ans
0
0


                    