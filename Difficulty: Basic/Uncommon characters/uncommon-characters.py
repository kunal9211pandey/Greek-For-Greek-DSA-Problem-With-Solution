class Solution:
    def uncommonChars(self, s1, s2):
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in s2:
            freq2[ord(ch) - ord('a')] += 1

        result = []

        for i in range(26):
            if (freq1[i] > 0 and freq2[i] == 0) or (freq1[i] == 0 and freq2[i] > 0):
                result.append(chr(i + ord('a')))

        return "".join(result)
