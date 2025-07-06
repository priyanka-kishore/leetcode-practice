class Solution:
    # O(n) time, O(n) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = max_len = 0
        seen = set()

        while R < len(s):
            # if R char is not dupe, add to set, move R++, increase max
            if s[R] not in seen:
                seen.add(s[R])
                curr_len = R - L + 1
                max_len = max(curr_len, max_len)
                R += 1
            else:
                # move Left pointer up one
                seen.remove(s[L])
                L += 1

        return max_len