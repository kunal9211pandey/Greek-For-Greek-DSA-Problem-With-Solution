class Solution:
    def findCeil(self, arr, x):
        left = 0
        right = len(arr) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
