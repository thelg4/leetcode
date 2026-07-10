class Solution(object):
    def sumAndMultiply(self, n):
        x = 0
        place = 1
        total = 0

        while n > 0:
            digit = n % 10
            n //= 10

            if digit != 0:
                x += digit * place
                total += digit
                place *= 10

        return total * x
