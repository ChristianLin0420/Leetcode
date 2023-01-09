class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a = ""

        for i in order:
            a += i * s.count(i)

        for i in s:
            if i not in order:
                a += i
                
        return a