class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        x=len(nums)
        for i in range(x):
            base=i
            for j in range(i+1,x):
                if nums[base]+nums[j] == target:
                    result.append(base)
                    result.append(j)
        
        return result
        
        