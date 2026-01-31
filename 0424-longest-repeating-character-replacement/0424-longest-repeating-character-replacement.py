class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        L = 0
        max_len = 0
        max_freq = 0

        for R in range(len(s)):
            # save 2 states: char counts and count of most frequent char (don't need to know which one)
            char_count[s[R]] = char_count.get(s[R], 0) + 1
            max_freq = max(max_freq, char_count[s[R]]) # this is the tricky part i couldn't get to!

            # valid = size of dict is max (k + 1) and count of most freq char == window len - k
            if len(char_count) <= k + 1 and max_freq >= (R - L + 1) - k:
                max_len = max(max_len, R - L + 1)
            else:
                char_count[s[L]] -= 1
                if char_count[s[L]] == 0:
                    del char_count[s[L]]
                L += 1

        return max_len
