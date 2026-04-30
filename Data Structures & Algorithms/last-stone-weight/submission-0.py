class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Turn all stones negative to simulat a Max-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # Smash stones while more than 1 remains
        while len(max_heap) > 1:
            # Pop the two largest stones (most negative)
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # If they aren't eqaul, push the remainder back
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        # Return the last stone's weight, or 0 if none left
        return -max_heap[0] if max_heap else 0