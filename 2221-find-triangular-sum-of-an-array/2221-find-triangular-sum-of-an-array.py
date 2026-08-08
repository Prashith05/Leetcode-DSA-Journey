class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1

        return nums[0]