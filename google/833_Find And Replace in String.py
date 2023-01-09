class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        for ind , sor , tar in sorted(list(zip(indices,sources,targets)) ,key =  lambda x : x[0] ,reverse = True):
            if s[ind:ind+len(sor)] == sor:
                s = s[:ind] + tar + s[ind+len(sor):]

        return s

        