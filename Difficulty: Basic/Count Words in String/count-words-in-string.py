class Solution:
    def countWords(self, s):
        if s == '':
            return 0

        count = 1
        for ch in s:
            if ch == ' ':
                count += 1

        return count
