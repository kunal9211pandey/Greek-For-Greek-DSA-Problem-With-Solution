class Solution:
    def findSum(self, arr):
        seen = set()
        total_sum = 0
        
        for num in arr:
            if num not in seen:
                seen.add(num)
                total_sum += num
        return total_sum
