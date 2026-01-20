class SolutionOneString:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

class SolutionLastIndex:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        for i in range(last, -1, -1):
            if s[i] != ' ':
                break
        length = 0
        for j in range(i, -1, -1):
            if s[j] == ' ':
                break
            length += 1
        return length

