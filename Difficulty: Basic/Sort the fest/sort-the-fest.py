#User function Template for python3


class Solution:
    def is_common(self, s, t):
        # Code here
        for ch in s:
            if ch in t:
                return "CHANGE"
        return "BEHAPPY"