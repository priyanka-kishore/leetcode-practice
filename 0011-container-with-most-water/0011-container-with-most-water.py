class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1

        while l < r:
            # 1. area = smaller edge * (r - l)
            # 2. calculate if curr area is max
            # 3. to maximize next iteration, keep tallest edge, move other pointer

            currArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currArea)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea