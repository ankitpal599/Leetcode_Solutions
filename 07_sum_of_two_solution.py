#Given an integer n, return true if it is a power of two. Otherwise, return false.
#An integer n is a power of two, if there exists an integer x such that n == 2x.
class Solution(object):
    def isPowerOfTwo(self, n):
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
            power *= 2
        return False
