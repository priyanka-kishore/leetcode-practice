class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        seen_with_idx = {}
        window_sum = 0
        max_sum = 0

        for end in range(len(nums)):
            window_sum += nums[end]

            ## Adjust window to maintain uniqueness
            
            # if already seen, move start to AFTER that seen index ONLY IF seen index >= START
            if nums[end] in seen_with_idx:
                while start <= seen_with_idx[nums[end]]:
                    window_sum -= nums[start]
                    start += 1

            # update set with currently seen index
            seen_with_idx[nums[end]] = end
            
            ## Calculate state and adjust sliding window for next iteration
            
            if end - start + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[start]
                start += 1

        return max_sum
        