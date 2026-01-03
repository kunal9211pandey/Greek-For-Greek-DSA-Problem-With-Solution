# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for num in arr:
        original = num
        rev = 0
        
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
            
        if rev != original:
            return False
            
    return True
            