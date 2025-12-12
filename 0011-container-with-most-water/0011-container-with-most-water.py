class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0

        while i < j:
            containerLen = j - i
            containerHeight = min(height[i], height[j])
            maxArea = max(containerLen * containerHeight, maxArea)

            # print(f"{height[i]},{height[j]}: len={containerLen} height={containerHeight} area={containerLen * containerHeight} maxArea={maxArea}")

            if height[i] > height[j]:
                j -= 1
            else: 
                i += 1
            
        return maxArea
        