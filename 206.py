

## REVERSE A GIVEN LINKED LIST at HEAD


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = head
        if (last == None) or (last.next == None):
            return last
        curr = last.next
        last.next = None
        while True:
            dummy = curr.next
            curr.next = last
            if dummy == None:
                return curr
            last,curr = curr, dummy


""" 
Runtime: 44 ms, faster than 54.21% of Python3 online submissions.
Memory Usage: 15 MB, less than 28.32% of Python3 online submissions.
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head == None) or (head.next == None):
            return head
        curr = head.next
        head.next = None
        while True:
            dummy = curr.next
            curr.next = head
            if dummy == None:
                return curr
            head,curr = curr, dummy


"""
Runtime: 36 ms, faster than 95.00% of Python3 online submissions.
Memory Usage: 15 MB, less than 28.32% of Python3 online submissions.
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return head
        sol = ListNode(head.val)
        while head.next != None:
            dummy = ListNode(head.next.val)
            dummy.next = sol
            sol = dummy
            head = head.next
        return sol


"""
Runtime: 44 ms, faster than 54.21% of Python3 online submissions for Reverse Linked List.
Memory Usage: 16.1 MB, less than 22.38% of Python3 online submissions for Reverse Linked List.
"""



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head == None) or (head.next == None):
            return head
        rest = head.next
        reverse = self.reverseList(rest)
        rest.next = head
        head.next = None
        return reverse


"""
Runtime: 44 ms, faster than 54.21% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19.6 MB, less than 8.52% of Python3 online submissions for Reverse Linked List.
"""

