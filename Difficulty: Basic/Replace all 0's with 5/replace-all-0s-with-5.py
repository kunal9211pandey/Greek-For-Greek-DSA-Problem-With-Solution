# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        if n == 0:
            return 5
            
        result = 0
        place = 1
        
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5
            
            result = result + digit * place
            place = place * 10
            n = n // 10
            
        return result