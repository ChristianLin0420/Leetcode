class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        cur = ""
        k = 0
        for c in s:
            if c == "[":
                stack.append((cur, k))
                cur, k = "", 0 # reset global vars
            elif c == "]":
                enc, n = stack.pop()
                cur = enc + n * cur 
            elif c.isdigit():
                k = k * 10 + int(c) # for two and three digit numbers
            else:
                cur += c # track the lower case letters
                
        return cur
                    


