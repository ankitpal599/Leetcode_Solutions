#An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
#Given an integer n, return true if n is an ugly number.
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n%p == 0:
                n //= p
        return n == 1
