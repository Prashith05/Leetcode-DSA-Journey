class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        best = ""

        for i in range(len(s)):
            ones = 0

            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    curr = s[i:j+1]

                    if best == "" or len(curr) < len(best):
                        best = curr
                    elif len(curr) == len(best) and curr < best:
                        best = curr

                    break

        return best
    