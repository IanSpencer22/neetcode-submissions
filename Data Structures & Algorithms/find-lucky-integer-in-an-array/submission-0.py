class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        result = -1
        for num, count in freq.items():
            if num == count:
                result = max(result, num)
        
        return result
        