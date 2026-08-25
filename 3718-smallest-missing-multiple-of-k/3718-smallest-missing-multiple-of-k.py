class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        x=k

        while x in nums:
            x+=k
        return x


        # nums.sort()
        # new=[]
        # for num in nums:
        #     if k*num not in nums:
        #         new.append(k*num)


        # return min(new)

        # nums.sort()
        # ktable=[]
        # for i in range(len(nums)):
        #     ktable.append(k*(i+1))
        # for j in range(len(nums)):
        #     if ktable[j] != nums[j]:
        #         return ktable[j]




