class Solution:
    # O(n) time, O(1) space
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        for n in nums[:k]:
            sums += n
        max_avg = sums / k
        
        i = 1
        while i + k - 1 < len(nums):
            sums = sums - nums[i-1] + nums[i + k - 1]
            max_avg = max(sums/k, max_avg)
            i += 1

        return max_avg