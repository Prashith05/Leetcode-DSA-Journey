class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        vals = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        result = vals[s[0]]

        for i in range(1,len(s)):
            if vals[s[i - 1]] < vals[s[i]]:
                result += vals[s[i]] - vals[s[i-1]]*2
                
            else:
                result += vals[s[i]]

        return result


        # vals = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        # result = 0



        # # for i in range(len(s)):
        #     if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:
        #         result -= vals[s[i]]
        #     else:
        #         result += vals[s[i]]

        # return result

        