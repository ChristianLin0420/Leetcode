class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        waiting = defaultdict(list)
        count = 0

        for word in words:
            waiting[word[0]].append(word[1:])

        for c in s:
            if c not in waiting:
                continue

            remainders = waiting[c]
            waiting[c] = []

            for remainder in remainders:
                if remainder == "":
                    count += 1
                else:
                    waiting[remainder[0]].append(remainder[1:])

        return count