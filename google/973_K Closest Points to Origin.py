class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [sqrt(x**2 + y**2) for x, y in points]
        dictDistances = {}
        for key, value in zip(distances, points):
            if (key in dictDistances):
                dictDistances[key] += [value]
            else:
                dictDistances[key] = [value]

        closestPoints = []
        count = 0
        for dist in sorted(distances):
            for point in dictDistances[dist]:
                if (count == k):
                    return closestPoints
                closestPoints.append(point)
                count += 1
        return [[]]