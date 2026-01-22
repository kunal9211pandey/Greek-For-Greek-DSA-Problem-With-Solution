class Solution:
    def calculateFriendliness(self, arr):
        n = len(arr)
        if n <= 1:
            return 0

        sum_value = 0

        for i in range(n):
            next_idx = (i + 1) % n
            sum_value += abs(arr[i] - arr[next_idx])

        return sum_value
