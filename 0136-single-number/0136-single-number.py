class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0

        for num in nums:
            #same value makes the XOR to zero(False), diffenent vlaues is One(True), since only one value is unique
            result ^= num
        
        return result