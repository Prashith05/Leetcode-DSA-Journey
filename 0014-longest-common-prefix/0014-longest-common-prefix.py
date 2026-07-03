class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # prefix = strs[0]
        # pre=""
        # for i in range(1,len(strs)):
        #     for j in range(min(len(perfix),len(strs[i]))):
        #         if prefix[j] == strs[i][j]:
        #             pre += prefix[j]
        # return prefix
    
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(1,len(strs)):
            pre=""
            for j in range(min(len(prefix),len(strs[i]))):
                if prefix[j] == strs[i][j]:
                    pre += prefix[j]
                else:
                    break
            prefix = pre
        return prefix
        