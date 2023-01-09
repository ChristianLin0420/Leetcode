class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sol = []
        res = []
        products.sort()
        for i in range(len(searchWord)):
            searched = searchWord[0:i+1]
            for item in products:
                if item[0:i+1] == searched:
                  res.append(item)
            products = res
            if len(res) >= 3:
                res = res[0:3]
            sol.append(res)
            res = []
        return sol