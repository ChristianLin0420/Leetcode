class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        outgoing = defaultdict(list)
        ingoing = defaultdict(int)

        for pre_n, next_n in relations:
            outgoing[pre_n].append(next_n)
            ingoing[next_n] += 1

        top = []

        for i in range(1, n + 1):
            if i not in ingoing:
                top.append(i)

        result = 0
        new_top = []
        visited_nodes = set()

        while top:
            node = top.pop(0)
            visited_nodes.add(node)

            for next_n in outgoing[node]:
                ingoing[next_n] -= 1
                if ingoing[next_n] == 0:
                    new_top.append(next_n)

            if not top:
                top = new_top
                new_top = []
                result += 1

        return result if len(visited_nodes) == n else -1
                    