class Solution:
    def maxAdj(self, arr):
        i = 0
        j = 1
        result = []

        while j < len(arr):
            if arr[i] > arr[j]:
                result.append(arr[i])
            else:
                result.append(arr[j])
            i += 1
            j += 1

        return result
