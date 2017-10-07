'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome_root_list = []
        p_c = ''
        pp_c = ''
        s_len = len(s)

        for i, c in enumerate(s):
            palindrome_root_list.append([1, i])
            if p_c == c:
                palindrome_root_list.append([2, i])
            if pp_c == c:
                palindrome_root_list.append([3, i])

            pp_c = p_c
            p_c = c

        longest_result = ''
        for pair in palindrome_root_list:
            if pair[0] == 2:
                r_index = pair[1]
                l_index = pair[1] - 1
                result = ''

            if pair[0] == 3:
                r_index = pair[1]
                m_index = pair[1] - 1
                l_index = pair[1] - 2
                m_c = s[m_index]

                result = m_c

            if pair[0] == 1:
                m_index = pair[1]
                m_c = s[m_index]

                result = m_c
            
            while pair[0] == 2 or pair[0] == 3:
                if r_index >= s_len or l_index < 0:
                    break

                r_c = s[r_index]
                l_c = s[l_index]

                if r_c != l_c:
                    break

                result = l_c + result + r_c
                
                r_index += 1
                l_index -= 1
  
            if len(result) > len(longest_result):
                longest_result = result

        return longest_result