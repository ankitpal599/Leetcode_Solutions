#Given an integer n, return true if it is a power of four. Otherwise, return false.
#An integer n is a power of four, if there exists an integer x such that n == 4x.
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        power = 1
        while power <= n:
            if power == n:
                return True
            power *= 4
        return False
        