'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        
        thousand = int(num/1000)
        hundred = int((num % 1000)/100)
        ten = int((num % 100)/10)
        one = int((num % 10)/1)

        result += "M" * thousand

        if hundred == 9:
            result += "CM"
        elif hundred == 4:
             result += "CD"
        else:
            result += "D" * int(hundred / 5)
            result += "C" * int(hundred % 5)

        if ten == 9:
            result += "XC"
        elif ten == 4:
             result += "XL"
        else:
            result += "L" * int(ten / 5)
            result += "X" * int(ten % 5)

        if one == 9:
            result += "IX"
        elif one == 4:
             result += "IV"
        else:
            result += "V" * int(one / 5)
            result += "I" * int(one % 5)

        return result