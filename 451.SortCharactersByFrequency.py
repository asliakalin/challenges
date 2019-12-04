"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] = dic[i] + str(i)
            else:
                dic[i] = str(i)
                
        arr = dic.values()
        arr = sorted(arr, key=lambda val: -len(val))
        return "".join(str(c) for c in arr)