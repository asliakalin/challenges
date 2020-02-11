"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""

# IF WE CAN ASSUME EACH NODE VALUE IS UNIQUE 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        destinations = set()
        return self.hasCycleHelper(head, destinations)
        
    
    def hasCycleHelper(self, h, dest):
        if (h == None) or (h.next == None):
            return False
        elif h.val in dest:   # is already reachable by another node
            return True
        else:
            dest.add(h.next.val)
            return self.hasCycleHelper(h.next, dest)
        
        
# IF WE CAN NOT ASSUME EACH NODE VALUE IS UNIQUE

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
                



"""
Runtime: 32 ms, faster than 95.00% of Python online submissions for Linked List Cycle.
Memory Usage: 18.4 MB, less than 26.24% of Python online submissions for Linked List Cycle.
"""








