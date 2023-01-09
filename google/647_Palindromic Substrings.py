class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        res=n

        if n==1:
            return res
            
        def getPalindromes(i,j):
            count=0
            while s[i]==s[j]:
                count+=1
                if i==0 or j==n-1:
                    break
                i-=1
                j+=1
            
            return count

        for i in range(1,len(s)-1):
            res+= getPalindromes(i-1,i+1) + getPalindromes(i-1,i)
        
        res+=getPalindromes(n-2,n-1)

        return res