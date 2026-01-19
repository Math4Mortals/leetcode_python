class SolutionHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        observed = {}
        for i, num in enumerate(nums):
            need_num = target - num
            if need_num in observed:
                return [observed[need_num], i]
            observed[num] = i

class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

class SolutionTwoPointers:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(val, i) for i, val in enumerate(nums)]
        arr.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        while left < right:
            s = arr[left][0] + arr[right][0]
            if s == target:
                return [arr[left][1],arr[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1
