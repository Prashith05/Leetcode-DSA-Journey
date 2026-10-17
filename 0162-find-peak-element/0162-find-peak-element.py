class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since any one peak can be returned and need to be in O(log n) i am goin to write in binary search

        # lineatsearch = O(n)
        # binary search =O(log n)

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left



        # if find the peak element from the list and the list has two elements we can use this method 

        # if not nums:
        #     return -1
        
        # max=nums[0]
        # max_index = 0

        # for i,num in enumerate(nums):
        #     if max < num:
        #         max = num
        #         max_index = i
        # return max_index