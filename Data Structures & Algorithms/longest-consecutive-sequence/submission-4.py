class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = 1
        seen = set()
        for i in range(len(nums)):
            start = nums[i]
            end = nums[i]
            seen.add(start)
            temp = 1

            while start - 1 in seen or end + 1 in seen:
                if start - 1 in seen:
                    temp += 1
                    start -= 1
                if end + 1 in seen:
                    temp += 1
                    end += 1
                
                if temp >= res:
                    res = temp


        return res
        