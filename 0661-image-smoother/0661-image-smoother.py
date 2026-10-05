class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                total = 0
                count = 0

                # Check the 3 x 3 area around (i, j)
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:

                        ni = i + di
                        nj = j + dj

                        # Check if neighbor is inside the matrix
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                result[i][j] = total // count

        return result
