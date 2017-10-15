'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
 
        if numRows == 1:
            numColumns = len(s)
            interval = 1
        else:
            numColumns = int(len(s) / (2 + 2 * (numRows-2))) + 1
            interval = (2 * (numRows - 2) + 1 + 1)

        for i in range(0, numColumns):
            s_index = i * interval
            if s_index < len(s):
                result += s[s_index]
        
        for j in range(1, numRows - 1):
            for i in range(0, numColumns):
                s_index = i * interval + j
                if s_index < len(s):
                    result += s[s_index]
                
                s_index = (i+1) * interval - j
                if s_index < len(s):
                    result += s[s_index]
        
        if numRows != 1:
            for i in range(0, numColumns):
                s_index = i * interval + numRows -1
                if s_index < len(s):
                    result += s[s_index]
        
        return result