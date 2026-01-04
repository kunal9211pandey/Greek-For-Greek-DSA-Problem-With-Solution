class Solution:
    def removeDuplicate(self, arr):
        seen = set()
        result = []

        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)

        return result
