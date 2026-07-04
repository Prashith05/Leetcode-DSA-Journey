class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Pascal = [[1],[1,1]]

        if numRows == 1:
            return [[1]]
            
        if numRows == 2:
            return Pascal

        for i in range(1,numRows - 1):
            holder = []

            for j in range(1,len(Pascal[i])):  # ranging the previous pascal value(end value)
                holder.append(Pascal[i][j] + Pascal[i][j-1])

            Pascal.append([1]+holder+[1])
            
        return Pascal


        