class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        all_people = [i+1 for i in range(n)]

        pointer = 0

        while len(all_people) > 1:
            pointer = (pointer + k - 1) % len(all_people)
            all_people.pop(pointer)
            
        return all_people[0]
                