class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs) # O(nlogn)
        l = 0
        r = len(logs) - 1
        ans = -1
        while l<= r:  # O(logn)
            mid = (r+l) // 2
            if self.is_connected(logs[:mid+1], n):  # O(n)
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        if ans == -1:
            return -1

        return logs[ans][0]

    def is_connected(self, logs, n):
        # check if we have a connected graph
        g = collections.defaultdict(list)
        for t, p1, p2 in logs:
            g[p1].append(p2)
            g[p2].append(p1)

        seen = set()
        def dfs(node):
            seen.add(node)
            for next_node in g[node]:
                if next_node not in seen:
                    dfs(next_node)
            
        dfs(logs[0][1]) # start node can be anywhere
        return len(seen) == n