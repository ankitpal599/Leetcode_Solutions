#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a = 1
        b = 2
        c = 0
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c
        
 
