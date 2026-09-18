#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original_num = x
        reversed_num = 0
        if x < 0:
             return False
        while x > 0:
            remainder = x % 10
            reversed_num = reversed_num * 10 + remainder
            x //= 10
        return original_num == reversed_num
        