class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        max=nums[0]
        max_index = 0

        for i,num in enumerate(nums):
            if max < num:
                max = num
                max_index = i
        return max_index