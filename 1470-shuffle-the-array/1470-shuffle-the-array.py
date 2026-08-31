class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]
        y = nums[n:]
        nums=[]
        for i in range(n):
            nums.extend((x[i],y[i]))
        return nums

        