class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        
        for _ in range(len(nums)-1):
            subarr=[]

            for i in range(1,len(nums)):
                subarr.append((nums[i]+nums[i-1])%10)
            nums=subarr

        return nums[0]
