class Bomb:
    def __init__(self, x, y, r):
        self.coord = (x, y)
        self.radius = r
        self.neighbors = []

    def find_neighbors(self, nodes):
        for node in nodes:
            if node != self:
                dist = get_dist(self, node)
                if dist <= self.radius:
                    self.neighbors.append(node)

def get_dist(node1, node2):
    return math.sqrt((node1.coord[0] - node2.coord[0]) ** 2 + (node1.coord[1] - node2.coord[1]) ** 2)

def search_detonations(node):
    search = deque([node])
    seen = set()
    current = node

    while search:
        current = search.pop()
        if current not in seen:
            seen.add(current)
            for nd in current.neighbors:
                if nd not in seen:
                    search.appendleft(nd)

    return len(seen)

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        nodes = [Bomb(x, y, r) for x, y, r in bombs]
        result = 0

        for node in nodes:
            node.find_neighbors(nodes)

        for node in nodes:
            result = max(result, search_detonations(node))

        return result
            




