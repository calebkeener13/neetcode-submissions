class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # optimized solution
        first = 0
        second = 0
        countF = 0
        countS = 0

        for n in nums:
            if n == first:
                countF += 1
            elif n == second:
                countS += 1
            elif countF == 0:
                countF = 1
                first = n
            elif countS == 0:
                countS = 1
                second = n
            else:
                countF -= 1
                countS -= 1
                
        res = []  
        threshold = (len(nums) // 3)
        if countF > 0 and nums.count(first) > threshold:
            res.append(first)
        if countS  > 0 and nums.count(second) > threshold:
            res.append(second)
        return res
        