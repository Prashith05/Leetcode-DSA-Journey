class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen[num] =1


        slow = nums[0]
        fast = nums[0]

        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find entrance of cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
