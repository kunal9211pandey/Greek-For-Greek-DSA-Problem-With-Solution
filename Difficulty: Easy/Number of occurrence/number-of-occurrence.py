class Solution:
    def countFreq(self, arr, target):
        n = len(arr)

        # find first occurrence
        left, right = 0, n - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if first == -1:
            return 0

        # find last occurrence
        left, right = 0, n - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last - first + 1
