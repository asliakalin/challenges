
"""
Asli Akalin: 04/02/2019

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.
"""



## Super unefficient. OK for small s
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def checkSame(here):
            if len(here) != k:
                return False
            else:
                sample = here[0]
                for i in here:
                    if i != sample:
                        return False
                return True
        
        index = 0
        while index <= len(s)-k:
            if checkSame(s[index:index+k]):
                s = s[:index] + s[index+k:]
                index = 0 if (index <= k-1) else index - (k-1)
            else:
                index += 1 
        return s