import heapq

class Pair:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency > other.frequency

    def __gt__(self, other):
        return self.frequency < other.frequency

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        max_heap = [Pair(key, value) for key, value in hash_map.items()]
        heapq.heapify(max_heap)

        return [heapq.heappop(max_heap).key for _ in range(k)]