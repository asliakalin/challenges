"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if (m == 0):
            nums1[0] = nums2[0]
        else:
            index = m+n-1
            while m-1>=0 and n-1>=0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[index] = nums1[m-1]
                    m = m-1
                else:
                    nums1[index] = nums2[n-1]
                    n -= 1
                index -= 1  
        # add missing elements from nums2 
        nums1[:n] = nums2[:n] 