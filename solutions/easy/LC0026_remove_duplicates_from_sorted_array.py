class SolutionWhile:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pnt1 = 0
        pnt2 = pnt1 + 1
        while pnt2 < len(nums):
            if nums[pnt1] == nums[pnt2]:
                pnt2 += 1
            else:
                pnt1 += 1
                nums[pnt1] = nums[pnt2]
                pnt2 += 1
        return pnt1 + 1

class SolutionFor:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pnt1 = 0
        for pnt2 in range(1, len(nums)):
            if nums[pnt1] != nums[pnt2]:
                pnt1 += 1
                nums[pnt1] = nums[pnt2]
        return pnt1 + 1
