class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,num in enumerate(nums):
            key = target - num 

            if key in seen:
                return[seen[key],i]
            seen[num]=i    
        