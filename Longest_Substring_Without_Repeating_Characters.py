'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_c_dict = {}
        postfix_index = 0
        suffix_index = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in curr_c_dict:
                if curr_c_dict[c] + 1 > postfix_index:
                    postfix_index = curr_c_dict[c] + 1

            curr_c_dict.update({c : i})
            suffix_index = i

            if len(s[postfix_index : suffix_index + 1]) > max_length:
                max_length = len(s[postfix_index : suffix_index + 1])

        return max_length