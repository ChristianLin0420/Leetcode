class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n-1):
            conversion = []
            converted_num = n

            while converted_num > 0:
                conversion.append(converted_num % b)
                converted_num /= b

            if conversion != conversion[::-1]: 
                return False

        return True