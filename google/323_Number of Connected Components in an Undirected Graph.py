class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ans = 0
        visited_nodes = set()

        def dfs(node: int):
            for neighbor in graph[node]:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    dfs(neighbor)
            
        for i in range(n):
            if i not in visited_nodes:
                visited_nodes.add(i)
                ans += 1
                dfs(i)

        return ans