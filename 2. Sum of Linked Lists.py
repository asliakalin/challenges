
# sum two numbers in linked lists in reverse order of digits

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode(-1)
        dig = curr
        l3 = 0
        while l1 or l2: 
            val = None
            if l1 == None:
                if (l2.val + l3) < 10: 
                    val = ListNode(l2.val + l3)
                    l3 = 0
                else: 
                    val =ListNode((l2.val + l3)%10)
                    l3 = (l2.val + l3)//10
                l2 = l2.next
            elif l2 == None:
                if (l1.val + l3) < 10: 
                    val = ListNode(l1.val + l3)
                    l3 = 0
                else: 
                    val =ListNode((l1.val + l3)%10)
                    l3 = (l1.val + l3)//10
                l1 = l1.next
            else:
                if (l2.val + l1.val + l3) < 10:
                    val = ListNode(l2.val + l1.val +l3)
                    l3 = 0
                else:
                    val = ListNode((l2.val + l1.val + l3)%10)
                    l3 = (l2.val + l1.val + l3)//10
                l1 = l1.next
                l2 = l2.next
            dig.next = val
            dig = dig.next
        if l3 != 0:
            dig.next = ListNode(l3)
        return curr.next




        """Runtime: 72 ms, faster than 91.61% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 5.20% of Python3 online submissions for Add Two Numbers."""




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode(-1)
        dig = curr
        l3 = 0
        while l1 or l2 or (l3 != 0): 
            val = None
            if l1 == None:
                val = (0 if l2==None else l2.val) + l3
                l2 = (None if l2==None else l2.next)
            elif l2 == None:
                val = l1.val + l3
                l1 = l1.next
            else:
                val = l1.val + l2.val + l3
                l1 = l1.next
                l2 = l2.next    
            v = ListNode(val%10)
            l3 = (val)//10
            dig.next = v
            dig = dig.next
        return curr.next


 """
 Runtime: 76 ms, faster than 77.57% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 5.20% of Python3 online submissions for Add Two Numbers.
"""