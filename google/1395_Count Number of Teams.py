class Solution:
    def numTeams(self, rating: List[int]) -> int:

        length = len(rating)
        right_recorder = [0] * length
        left_recorder = [0] * length
        result = 0

        for i in range(length):
            for j in range(i, length):
                if rating[i] > rating[j]:
                    right_recorder[i] += 1

        for i in range(length):
            for j in range(i):
                if rating[i] > rating[j]:
                    left_recorder[i] += 1

        for i in range(length):
            for j in range(i, length):
                if rating[i] > rating[j]:
                    result += right_recorder[j]

        for i in range(length):
            for j in range(i):
                if rating[i] > rating[j]:
                    result += left_recorder[j]

        return result
