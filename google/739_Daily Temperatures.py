class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp = temperatures
        answer = [0]*len(temp)
        q = []

        q.append( (temp[0], 0))

        for i in range(1, len(temp)):

            curr = temp[i]

            while q and curr>q[-1][0]:

                lastTemp, lastIndex = q.pop()

                answer[lastIndex] = i-lastIndex

            q.append((curr, i))

        return answer


