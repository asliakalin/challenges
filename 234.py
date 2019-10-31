
# Given a singly linked list, determine if it is a palindrome.
# Could you do it in O(n) time and O(1) space?


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        size = 0
        dummy = head
        while dummy != None:
            dummy = dummy.next
            size += 1
        
        while size>=0:
            if size <= 2:
                if ((size == 2) and (head.val != head.next.val)):
                    return False
                else:
                    return True
            even = ((size%2) == 0)
            mid = (size/2)-2 if even else ((size)//2)-1
            sym, prev = head, head
            while mid > 0:
                prev = prev.next
                mid -= 1
            sym = prev.next
            if even: 
                if (sym.val != sym.next.val):
                    return False
                else:
                    prev.next = sym.next.next
                    size -= 2
            else:
                prev.next = sym.next
                size -= 1 

""" Runtime Error """


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = ListNode(-1)
        size = 0
        dummy = head
        while dummy != None:
            dummy = dummy.next
            size += 1
        if size == 0: 
            return True
        if size == 1: 
            return True
        for i in range((size//2)):
            first = head
            head = head.next
            first.next = stack
            stack = first
        if (size % 2) == 1:
            head = head.next
        while stack != None and head != None:
            if stack.val != head.val:
                return False
            stack = stack.next
            head = head.next
        return True



"""
Runtime: 76 ms, faster than 77.27% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.4 MB, less than 8.50% of Python3 online submissions for Palindrome Linked List.
"""