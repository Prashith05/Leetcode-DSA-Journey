class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        x=[]
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                x.append(nums[i])
        return x