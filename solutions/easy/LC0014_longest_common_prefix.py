class SolutionSortWords:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sorted_strs = sorted(strs)
        common_prefix = ''
        first, last = sorted_strs[0], sorted_strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            common_prefix += first[i]
        return common_prefix
