class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        count = 0
        for num, k in freq.items():
            count += k * (k - 1) // 2        

        return count