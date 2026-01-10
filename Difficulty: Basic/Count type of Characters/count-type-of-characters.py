class Solution:
    def count(self, s):
        upper = lower = digit = special = 0

        for ch in s:
            if ch.isupper():
                upper += 1
            elif ch.islower():
                lower += 1
            elif ch.isdigit():
                digit += 1
            else:
                special += 1

        return upper, lower, digit, special
