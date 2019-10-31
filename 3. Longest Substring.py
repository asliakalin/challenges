
"""
Given a string, find the length of the longest substring 
without repeating characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0]*len(s)
        cur_max = 0
        cur = 0
        index = len(s)-1
        seen = {}
        while index>=0:
            if s[index] in seen.keys():
                if arr[index+1] < seen[s[index]] - index:
                    arr[index] = arr[index+1] + 1
                else:
                    arr[index] = seen[s[index]] - index
                cur = arr[index]
            else:
                cur += 1
                arr[index] = cur
            seen[s[index]] = index
            if arr[index] > cur_max:
                cur_max = arr[index]
            index -= 1
        return cur_max