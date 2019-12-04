"""
Given a non-empty array of integers, return the k most frequent elements.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        vals = {}
        for i in nums:
            if i in vals.keys():
                vals[i] += 1
            else:
                vals[i] = 1
        arr=sorted(vals.keys(), key= lambda val: -vals[val])
        return arr[:k]