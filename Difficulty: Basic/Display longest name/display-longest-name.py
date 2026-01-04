
class Solution:
    def longest(self, arr):
        # code here
        longest = ""
        
        for word in arr:
            if len(word) > len(longest):
                longest = word
        return longest