class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        # XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]

        max_xor = current_xor

        # Slide the window
        for i in range(k, n):
            current_xor ^= arr[i - k]  # remove left element
            current_xor ^= arr[i]      # add right element

            if current_xor > max_xor:
                max_xor = current_xor

        return max_xor
