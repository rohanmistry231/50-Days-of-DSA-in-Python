import heapq

class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)

# Example:
pq = MinPriorityQueue()
pq.insert(10)
pq.insert(5)
pq.insert(15)
pq.insert(2)

print("Min value:", pq.extract_min())  # Output: 2
print("Min value:", pq.extract_min())  # Output: 5
