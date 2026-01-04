class Solution:
    def maxDays(self, arr):
        max_candle = 0

        for num in arr:
            if num > max_candle:
                max_candle = num

        return max_candle
