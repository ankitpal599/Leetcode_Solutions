#Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
#For example:
#A -> 1
#B -> 2
#C -> 3
#Z -> 26
#AA -> 27
#AB -> 28 
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for letter in columnTitle:
            value = ord(letter) - ord('A') + 1
            result = result * 26 + value
        return result 
