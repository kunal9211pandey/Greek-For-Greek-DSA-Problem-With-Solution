class Solution:
    def modify(self, s):
        i = 0
        j = len(s) - 1
        vowels = ['a','e','i','o','u']
        char_list = list(s)

        while i < j:
            if char_list[i] not in vowels:
                i += 1
            elif char_list[j] not in vowels:
                j -= 1
            else:
                char_list[i], char_list[j] = char_list[j], char_list[i]
                i += 1
                j -= 1

        return "".join(char_list)
