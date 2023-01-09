class HitCounter:

    def __init__(self):
        self.hit_counter = {}

    def hit(self, timestamp: int) -> None:
        self.hit_counter[timestamp] = self.hit_counter.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for time, hit_count in self.hit_counter.items():
            if timestamp - 300 < time:
                hits += hit_count
        
        return hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)