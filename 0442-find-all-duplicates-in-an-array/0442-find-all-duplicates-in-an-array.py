class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        result = []

        for x in nums:
            i = abs(x) - 1

            if nums[i] < 0:
                result.append(abs(x))
            else:
                nums[i] = -nums[i]

        return result
