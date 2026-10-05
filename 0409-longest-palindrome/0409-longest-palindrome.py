class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1   # Counting the character

        result = 0
        has_odd = False

        # Use pairs
        for value in count.values():
            result += (value // 2) * 2

            # We can put one odd character in the middle
            if value % 2 == 1:
                has_odd = True

        if has_odd:
            result += 1

        return result
