class Solution:
    def convert(self, s):
        result = list(s)
        make_capital = True   # word start flag

        for i in range(len(result)):
            if result[i] == ' ':
                make_capital = True
            elif make_capital:
                result[i] = result[i].upper()
                make_capital = False

        return "".join(result)
