class SolutionDict:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = 1
        return False

class SolutionSet:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
