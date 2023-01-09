class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        chains = defaultdict(int)
        for word in words:
            addedWord = False
            for i in range(len(word)):
                wSlice = word[0:i] + word[i+1:]
                if wSlice in chains:
                    chains[word] = max(chains[word], chains[wSlice]+1)
                    addedWord = True
            if not addedWord:
                chains[word] = 1
        return max(chains.values())