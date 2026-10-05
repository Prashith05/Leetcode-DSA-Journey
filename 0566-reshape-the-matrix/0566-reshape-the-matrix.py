class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        # Cannot reshape if number of elements is different
        if m * n != r * c:
            return mat

        result = []
        row = []

        for i in range(m):
            for j in range(n):
                row.append(mat[i][j])

                # Once we have c elements, create a new row
                if len(row) == c:
                    result.append(row)
                    row = []

        return result