class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        graph_size = len(graph) - 1

        def dfs(current, path: List[int]):
            if current == graph_size:
                paths.append(path)

            for next in graph[current]:
                dfs(next, path + [next])

        dfs(0, [0])

        return paths