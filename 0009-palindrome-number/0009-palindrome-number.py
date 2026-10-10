class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        z=x
        rev=0
        while z>0:
            rev = (rev*10)+ (z%10)
            z//=10


        
        if rev == x:
            return True
        else:
            return False