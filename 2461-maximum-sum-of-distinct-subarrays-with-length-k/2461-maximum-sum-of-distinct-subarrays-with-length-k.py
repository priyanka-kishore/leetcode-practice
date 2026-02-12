class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        max_sum = 0
        win_sum, L = 0, 0

        for R in range(len(nums)):
            win_sum += nums[R]

            while nums[R] in seen:
                seen.remove(nums[L])
                win_sum -= nums[L]
                L += 1
            
            seen.add(nums[R])

            if R - L + 1 == k:
                max_sum = max(max_sum, win_sum)
                seen.remove(nums[L])
                win_sum -= nums[L]
                L += 1
        
        return max_sum