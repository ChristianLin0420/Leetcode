class MyCalendar:

    def __init__(self):
        self.booked = []
    
    def book(self, start:int, end:int):
        if len(self.booked) == 0:
            self.booked.append((start, end))
            return True
        else:
            return self.can_book(start, end)
    
    def can_book(self, start, end):
        low = 0
        high = len(self.booked) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if (self.booked[mid][0] < start < self.booked[mid][1]) or (self.booked[mid][0] < end < self.booked[mid][1]) \
                or (start <= self.booked[mid][0] and end >= self.booked[mid][1]):
                return False
            elif end <= self.booked[mid][0]:
                if mid - 1 < 0 or start >= self.booked[mid - 1][1]: # if we reach the beginning we can book
                    self.booked.insert(mid, (start, end)) # append the new booking
                    return True
                high = mid - 1
            elif end >= self.booked[mid][1]:
                if len(self.booked) == mid + 1 or end <= self.booked[mid + 1][0]: # if we reach the end we can book
                    self.booked.insert(mid + 1, (start, end))
                    return True
                low = mid + 1
        