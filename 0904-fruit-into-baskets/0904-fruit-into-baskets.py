class Solution:
    """
    Return the length of the largest subarray containing only 2 integers (or 2 characters).
    Example: 
        fruits = [3, 3, (2, 1, 2, 1), 0]
                         ^  ^  ^  ^ length = 4
    """
    def totalFruit(self, fruits: List[int]) -> int:
        L, max_len = 0, 0
        fruit_counts = {}

        for R in range(len(fruits)):
            # update set with current fruit
            fruit_counts[fruits[R]] = fruit_counts.get(fruits[R], 0) + 1 # Note - dict.get(value if in dict, default value if not in dict)

            # if window not valid, move L until valid
            while len(fruit_counts) > 2 and L < R:
                fruit_counts[fruits[L]] -= 1
                if fruit_counts[fruits[L]] == 0:
                    del fruit_counts[fruits[L]]
                L += 1

            # window is/becomes valid
            max_len = max(max_len, R - L + 1) # Note - don't need a "window_len"

        return max_len