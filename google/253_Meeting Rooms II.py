class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        min_heap = []
        max_room_reservation = 0

        for start, end in intervals:
            if not min_heap:
                min_heap.append(end)
            else:
                if start >= min_heap[0]:
                    heappop(min_heap)
                heappush(min_heap, end)

            max_room_reservation = max(max_room_reservation, len(min_heap))

        return max_room_reservation