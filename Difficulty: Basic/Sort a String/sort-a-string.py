class Solution:
    def sort(self, s):
        freq = [0] * 26

        # count characters
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # build sorted string
        result = []
        for i in range(26):
            while freq[i] > 0:
                result.append(chr(i + ord('a')))
                freq[i] -= 1

        return "".join(result)
