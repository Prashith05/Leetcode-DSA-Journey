class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        citizen = [0] * (n+1)
        judge = [0] * (n+1)

        for a,b in trust:
            citizen[a] += 1
            judge[b] +=1
        for person in range(1,n+1):
            if judge[person] == n-1 and citizen[person] == 0:
                return person
        return -1
