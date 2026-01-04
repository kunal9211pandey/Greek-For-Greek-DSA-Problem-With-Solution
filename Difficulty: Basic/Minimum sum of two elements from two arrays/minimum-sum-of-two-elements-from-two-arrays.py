class Solution:
    def minSum(self, arr1, arr2):
        n = len(arr1)

        min1 = float('inf')
        min1_idx = -1
        second_min1 = float('inf')

        min2 = float('inf')
        min2_idx = -1
        second_min2 = float('inf')

        # find smallest and second smallest in arr1
        for i in range(n):
            if arr1[i] < min1:
                second_min1 = min1
                min1 = arr1[i]
                min1_idx = i
            elif arr1[i] < second_min1:
                second_min1 = arr1[i]

        # find smallest and second smallest in arr2
        for i in range(n):
            if arr2[i] < min2:
                second_min2 = min2
                min2 = arr2[i]
                min2_idx = i
            elif arr2[i] < second_min2:
                second_min2 = arr2[i]

        # if indices are different
        if min1_idx != min2_idx:
            return min1 + min2

        # same index case
        return min(min1 + second_min2, second_min1 + min2)
