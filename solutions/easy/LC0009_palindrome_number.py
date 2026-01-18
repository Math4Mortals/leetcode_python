class SolutionSlice:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

class SolutionHalfReverse:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x != 0 and x % 10 == 0:
            return False

        half_rev = 0
        while x > half_rev:
            half_rev = half_rev * 10 + x % 10
            x //= 10

        return half_rev == x or half_rev // 10 == x

class SolutionFullReverse:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev_x = 0
        while num > 0:
            rev_x = rev_x * 10 + num % 10
            num //= 10
        return x == rev_x

class SolutionMirrorIndexes:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        len_str_x = len(str_x)
        for i in range(len_str_x // 2):
            if str_x[i] != str_x[len_str_x - i - 1]:
                return False
        return True

