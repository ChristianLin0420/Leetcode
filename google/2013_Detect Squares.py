class DetectSquares:

    def __init__(self):
        self.record = {}

    def add(self, point: List[int]) -> None:
        key = (point[0], point[1])

        if key in self.record:
            self.record[key] += 1
        else:
            self.record[key] = 1
        

    def count(self, point: List[int]) -> int:

        x, y = point[0], point[1]
        count = 0

        for (a, b) in self.record:
            if abs(x - a) == abs(y - b) and abs(x - a) != 0:
                count += self.record[(a, b)] * self.record.get((x, b), 0) * self.record.get((a, y), 0)

        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)