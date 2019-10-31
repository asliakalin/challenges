
# MERGE TWO ORDERED LINKED LISTS

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        val = None
        if (l1.val <= l2.val):
            val = l1.val
            l1 = l1.next
        else:
            val = l2.val
            l2 = l2.next
        first = ListNode(val)
        rest = self.mergeTwoLists(l1,l2)
        first.next = rest
        return first


"""
Runtime: 44 ms, faster than 64.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        val = None
        end = None
        if (l1.val <= l2.val):
            val,end = l1,l1
            while (l1.next != None) and (l1.next.val < l2.val):
                l1 = l1.next
                end = end.next
            save = l1.next
            l1 = save
        else:
            val,end = l2,l2
            while (l2.next != None) and (l2.next.val < l1.val):
                l2 = l2.next
                end = end.next
            save = l2.next
            l2 =save
        first = val
        rest = self.mergeTwoLists(l1,l2)
        end.next = rest
        return first

"""
Runtime: 44 ms, faster than 64.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        if (l1==None) and (l2 ==None): 
            return None
        while (l1 != None) or (l2 != None):
            if (l2 == None) or (l1 != None and l1.val <= l2.val):
                arr.append(ListNode(l1.val))
                l1 = l1.next
            else:
                arr.append(ListNode(l2.val))
                l2 = l2.next
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        return arr[0]


"""
Runtime: 48 ms, faster than 24.61% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        if (l1.val <= l2.val):
            first = l1
            while (l1.next != None) and (l1.next.val < l2.val):
                l1 = l1.next
            l1.next = self.mergeTwoLists(l1.next,l2)
        else:
            first = l2
            while (l2.next != None) and (l2.next.val < l1.val):
                l2 = l2.next
            l2.next = self.mergeTwoLists(l1,l2.next)
        return first
"""
Runtime: 40 ms, faster than 87.56% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



"""
Runtime: 48 ms, faster than 24.61% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        pos = ListNode(-1)
        prev = pos
        while (l1 != None) and (l2 != None):
            if (l1.val <= l2.val):
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2=l2.next
            prev = prev.next
        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1
        return pos.next

"""
Runtime: 44 ms, faster than 64.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
"""
