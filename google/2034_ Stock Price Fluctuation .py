class StockPrice:

    def __init__(self):
        self.timestamp = {}
        self.maxHeap = []
        self.minHeap = []
        self.maxTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:

        self.timestamp[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)

        heappush(self.maxHeap, (-price, timestamp))
        heappush(self.minHeap, (price, timestamp))
        
    def current(self) -> int:
        return self.timestamp[self.maxTimestamp]

    def maximum(self) -> int:
        (currentPrice, timestamp) = heappop(self.maxHeap)

        while -currentPrice != self.timestamp[timestamp]:
            (currentPrice, timestamp) = heappop(self.maxHeap)

        heappush(self.maxHeap, (currentPrice, timestamp))
        return -currentPrice    

    def minimum(self) -> int:
        (currentPrice, timestamp) = heappop(self.minHeap)

        while currentPrice != self.timestamp[timestamp]:
            (currentPrice, timestamp) = heappop(self.minHeap)

        heappush(self.minHeap, (currentPrice, timestamp))
        return currentPrice
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()