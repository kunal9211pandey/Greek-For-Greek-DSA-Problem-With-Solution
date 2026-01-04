class Solution:
    def findMaxOddSum(self, arr):
        total_sum = 0
        min_positive_odd = float('inf')
        max_negative_odd = float('-inf')

        for num in arr:
            if num > 0:
                total_sum += num
                if num % 2 != 0:
                    min_positive_odd = min(min_positive_odd, num)
            else:
                if num % 2 != 0:
                    max_negative_odd = max(max_negative_odd, num)

        # if total sum is already odd
        if total_sum % 2 != 0:
            return total_sum

        ans = -1

        # option 1: remove smallest positive odd
        if min_positive_odd != float('inf'):
            ans = max(ans, total_sum - min_positive_odd)

        # option 2: add largest negative odd
        if max_negative_odd != float('-inf'):
            ans = max(ans, total_sum + max_negative_odd)

        return ans
