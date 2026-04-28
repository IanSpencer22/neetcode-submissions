class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        items = list(counts.items())
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i][1] < items[j][1]:
                    items[i], items[j] = items[j], items[i]
        
        result = []
        for i in range(k):
            result.append(items[i][0])
        return result