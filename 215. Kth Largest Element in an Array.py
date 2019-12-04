"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = []
        # kth largest element has only k-1 things bigger than it, 
        # so the n - k - 1 things should be smaller than it
        # want k-1 smaller, n-k-1 bigger
        for i in range(len(nums)):
            if (not arr) or (len(arr) < k):
                heapq.heappush(arr, nums[i])
            else:
                smallest = heapq.heappop(arr)
                heapq.heappush(arr, max(nums[i], smallest))
        return heapq.heappop(arr)