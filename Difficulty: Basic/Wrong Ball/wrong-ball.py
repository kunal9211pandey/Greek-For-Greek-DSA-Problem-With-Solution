class Solution:
    def countWrongPlacedBalls(self, s):
        count = 0

        for i in range(len(s)):
            table_index = i + 1  # 1-based index

            if table_index % 2 == 0 and s[i] == 'R':
                count += 1
            elif table_index % 2 == 1 and s[i] == 'B':
                count += 1

        return count
