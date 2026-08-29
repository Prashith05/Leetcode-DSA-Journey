class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = 0
        for stone in stones:
            if stone in jewels:
                result += 1
        return result