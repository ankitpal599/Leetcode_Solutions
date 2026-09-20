#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_number = set()
        for n in nums:
            if n in unique_number:
                return True
            unique_number.add(n)
        return False       
