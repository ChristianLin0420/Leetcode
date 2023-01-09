class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.visited = [0]*(n+1)
        
        def backtrack(pos):
            if pos > n:  # we count 1only when we can reach to end
                self.count += 1
            for i in range(1, n+1):
                if not self.visited[i] and (i%pos==0 or pos%i==0):
                    self.visited[i] = 1
                    backtrack(pos+1)
                    self.visited[i] = 0
        
        backtrack(1)
        return self.count