class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if k == 1:
        #     return nums

        # l, r = 0, 0
        # res = [0]* (len(nums) - k + 1)

        # # initialize variables
        # first, second = 0, 0
        # firstI, secondI = -1, -1
        
        # #calculate max and secondMax of first window
        # while r < k:
        #     if nums[r] > second:
        #         if nums[r] > first:
        #             second = first
        #             secondI = firstI
        #             first = nums[r]
        #             firstI = r
        #         else:
        #             second = nums[r]
        #             secondI = r
        #     r += 1

        # res[l] = first
        # while r < len(nums):
        #     # if max is still in the window
        #     l += 1
        #     if firstI >= l:
        #         # only compare with the incoming element
        #         if nums[r] > first:
        #             second = first
        #             secondI = firstI
        #             first = nums[r]
        #             firstI = r

        #         elif nums[r] > first:
        #             second = nums[r]
        #             secondI = r
        #     else:
        #         # second is still in and the known highest
        #         if nums[r] > second:
        #             first = nums[r]
        #             firstI = r
        #         else:
        #             first = second
        #             firstI = secondI
            
        #     res[l] = first
        #     r += 1

        # return res

        #use max heap
        if k == 1:
            return nums

        l,r = 0, 0 
        window = []
        res = [0] * (len(nums) - k + 1)

        while r < k:
            heapq.heappush(window, (-nums[r], r))
            r += 1


        res[l] = -window[0][0]

        while r < len(nums):
            l += 1
            heapq.heappush(window, (-nums[r], r))
            while window and window[0][1] < l:
                heapq.heappop(window)

            res[l] = -window[0][0]
            r += 1
        return res
                
            


        




