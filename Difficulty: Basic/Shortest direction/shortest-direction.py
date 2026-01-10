class Solution:
    def shortestPath(self, s):
        countE = countW = countN = countS = 0

        for ch in s:
            if ch == 'E':
                countE += 1
            elif ch == 'W':
                countW += 1
            elif ch == 'N':
                countN += 1
            elif ch == 'S':
                countS += 1

        # net movements
        east = max(0, countE - countW)
        west = max(0, countW - countE)
        north = max(0, countN - countS)
        south = max(0, countS - countN)

        # lexicographically sorted result
        return (
            'E' * east +
            'N' * north +
            'S' * south +
            'W' * west
        )
