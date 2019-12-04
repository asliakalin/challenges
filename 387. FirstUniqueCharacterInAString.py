"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {}
        if len(s) ==0:
            return -1
        elif len(s) < 2:
            return 0
        else:
            for i in range(len(s)):
                val = s[i]
                if val in vals.keys():
                    vals[val] = -1
                else:
                    vals[val] = i
            #print([x for x in vals.values() if x!= -1])
            res = [x for x in vals.values() if x!= -1]
            return min(res) if res else -1