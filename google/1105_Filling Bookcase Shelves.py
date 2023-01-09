class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @functools.lru_cache(None)
        def dp(i):
            if i  >= len(books):
                return 0

            ans = float("inf")
            thck = 0
            height = 0
            for j in range(i, len(books)):
                thck +=  books[j][0]
                height = max(height, books[j][1])
                if thck >  shelfWidth:
                    break

                ans = min(ans, dp(j+1) + height)
            return ans


        return dp(0) 