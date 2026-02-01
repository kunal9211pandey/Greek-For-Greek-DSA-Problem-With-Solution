from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()      # indexes store karega
        result = []

        for i in range(len(arr)):

            # 1. Window se bahar wale index hatao
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. Chhote elements hatao (jo future me max nahi ban sakte)
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # 3. Current index add karo
            dq.append(i)

            # 4. Window complete hone par answer lo
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
