class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l == r:
                return [nums[l]]
            
            mid = (l + r) // 2

            return merge(mergeSort(l , mid), mergeSort(mid + 1, r))

        def merge(left, right):
            res = []

            l, r = 0, 0
            while l < len(left) and r < len(right):
                if (left[l] <= right[r]):
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            while l < len(left):
                res.append(left[l])
                l += 1

            while r < len(right):
                res.append(right[r])
                r += 1

            return res
        

        return mergeSort(0, len(nums) - 1)
