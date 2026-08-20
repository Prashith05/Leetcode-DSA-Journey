class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest



        # prefix = [0]*len(nums)
        # for i in range(len(nums)):
        #     prefix[i] +=nums[i]
        #     if prefix[i-1] < target and prefix[i] > target:
        #         return prefix[i]
        # return prefix[i]