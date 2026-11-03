class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in temp:
                return [temp[difference], i]

            temp[nums[i]] = i
        