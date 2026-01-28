class Solution:
    """
    Return the length of the largest subarray containing only 2 integers (or 2 characters).
    Example: 
        fruits = [3, 3, (2, 1, 2, 1), 0]
                         ^  ^  ^  ^ length = 4
    """
    def totalFruit(self, fruits: List[int]) -> int:
        L, max_len, window_len = 0, 0, 0
        fruit_counts = {}

        for R in range(len(fruits)):
            window_len += 1
            # update set with current fruit
            fruit_counts[fruits[R]] = fruit_counts[fruits[R]] + 1 if fruits[R] in fruit_counts else 1

            # window not valid
            if len(fruit_counts) > 2:
                while len(fruit_counts) > 2 and L < R:
                    fruit_counts[fruits[L]] -= 1
                    if fruit_counts[fruits[L]] == 0:
                        del fruit_counts[fruits[L]]
                    L += 1
                    window_len -= 1

            # window is/becomes valid
            max_len = max(max_len, window_len)

        return max_len