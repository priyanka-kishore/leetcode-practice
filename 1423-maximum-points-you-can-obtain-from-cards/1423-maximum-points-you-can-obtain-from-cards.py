class Solution:
    """
    solution ideas:
    - have fixed window of length = cards array length - k
    - cards IN the window cannot be picked as part of selection, so by exclusion, the outer cards outside the window are picked
        => THUS must MINIMIZE the sum of this window to MAXIMIZE sum of outer cards
    - then the max total of outer cards (PICKED) = total sum of cards array - sum of minimized window
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == 1:
            return cardPoints[0]

        # 1. get total sum of array : O(n) time
        total_points = sum(cardPoints) 
        if len(cardPoints) == k:
            return total_points
        
        # 2. get minimum sliding window of size (len(array) - k) : O(n) time
        min_sum = float('inf')
        window_sum = 0
        window_len = len(cardPoints) - k
        
        start = 0
        for end in range(len(cardPoints)):
            window_sum += cardPoints[end]

            if end - start + 1 == window_len:
                min_sum = min(min_sum, window_sum)
                window_sum -= cardPoints[start]
                start += 1
            
        # 3. return (total sum - min sliding window) : O(1) time
        return total_points - min_sum
