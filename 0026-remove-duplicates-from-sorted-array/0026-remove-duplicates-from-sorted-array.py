class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x +=1
        return x






        # j=0
        # for i in range(len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j+=1
        # return j
        