class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # digits[len(digits)-1] = digits[len(digits)-1] + 1
        # if digits[len(digits)-1] >= 10:
        #     digits.append(digits[len(digits)-1] % 10)
        #     digits[len(digits)-2] = 1
        # return digits

        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        return [1] + digits